from urllib.parse import unquote
from flask import redirect
from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info, Tag
from sqlalchemy.exc import IntegrityError
from model import *
from logger import logger
from schemas import *

# Import the schemas after importing the model
from model import Session
from model.cliente import Cliente
from model.preprocessador import PreProcessador
from model.carregador import Carregador
from model.avaliador import Avaliador
from model.pipeline import Pipeline
from model.modelo import Modelo

# Instanciando o objeto OpenAPI
info = Info(title="Minha API/Machine Learning", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
cliente_tag = Tag(name="Cliente", description="Adição, visualização, remoção de cliente")

# Rota home
@app.get('/', tags=[home_tag])

def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# Rota de listagem de Clientes
@app.get('/clientes', tags=[cliente_tag],
         responses={"200": ClienteViewSchema, "404": ErrorSchema})

def get_clientes():
    """Lista todos os clientes cadastrados na base
    Args:
       none 
    Returns:
        list: lista de clientes cadastrados na base
    """
    logger.debug("Coletando dados sobre todos os clientes")
    # Criando conexão com a base
    session = Session()
    # Buscando todos os clientes
    clientes = session.query(Cliente).all()
    
    if not clientes:
        logger.warning("Não há clientes cadastrados na base :/")
        return {"clientes": []}, 200
    else:
        logger.debug("%d Clientes encontrados", len(clientes))
        return apresenta_clientes(clientes), 200


# Rota de adição de cliente
@app.post('/cliente', tags=[cliente_tag],
          responses={"200": ClienteViewSchema, "400": ErrorSchema, "409": ErrorSchema})

def predict(form: ClienteSchema):
    """Adiciona um novo cliente à base de dados
    Retorna uma representação dos clientes e diagnósticos análise de credito.
    
    Args:
        nome_cliente                (str): nome do cliente
        idade                       (int): número que representa a idade
        sexo                        (str): sexo: "F" - feminino e "M" - masculino
        dependentes                 (int): dependentes
        escolaridade                (str): escolaridade
        estado_civil                (str): estado civil
        salario_anual               (float): salario Anual
        tipo_cartao                 (str): tipoCartao
        meses_de_relacionamento     (int): meses de relacionamento
        qtd_produtos                (int): qtd de Produtos
        iteracoes_12_meses          (int): iteracoes_12_meses
        meses_inativo_12_meses      (int): meses inativo em 12 meses
        limite_de_credito           (float): limite de credito
        valor_transacoes_12_meses   (float): valor de transacoes em 12 meses
        qtd_transacoes_12_meses     (int): qtd de transacoes em 12 meses        
        predicao_credito            (int): diagnostico do cliente: 0 - Adimplente e 1 - Inadimplente
    Returns:
        predicao_credito            (int): 0 representa diagnostico associado ao cliente: 0 - Adimplente e 1 Inadimplente
    """
    preprocessador = PreProcessador()
    carregador = Carregador()
    avaliador = Avaliador()
    pipeline = Pipeline()
    modelo = Modelo()

    # Recuperando os dados do formulário
    nome_cliente = form.nome_cliente
    idade = form.idade
    sexo = form.sexo
    dependentes = form.dependentes
    escolaridade = form.escolaridade
    estado_civil = form.estado_civil
    salario_anual = form.salario_anual
    tipo_cartao = form.tipo_cartao
    meses_de_relacionamento = form.meses_de_relacionamento
    qtd_produtos = form.qtd_produtos
    iteracoes_12_meses = form.iteracoes_12_meses
    meses_inativo_12_meses = form.meses_inativo_12_meses
    limite_de_credito = form.limite_de_credito
    valor_transacoes_12_meses = form.valor_transacoes_12_meses
    qtd_transacoes_12_meses = form.qtd_transacoes_12_meses
    
    # Preparando os dados para o modelo
    X_input = preprocessador.preparar_form(form)
    # Carregando pipeline
    model_path = './MachineLearning/pipelines/rf_credito_pipeline.pkl'
    pipeline = pipeline.carrega_pipeline(model_path)
    # Realizando a predição
    predicao_credito = int(modelo.preditor(pipeline, X_input)[0])
    
    cliente = Cliente(
        nome_cliente=nome_cliente,
        idade=idade,
        sexo=sexo,
        dependentes=dependentes,
        escolaridade=escolaridade,
        estado_civil=estado_civil,
        salario_anual=salario_anual,
        tipo_cartao=tipo_cartao,
        meses_de_relacionamento=meses_de_relacionamento,
        qtd_produtos=qtd_produtos,
        iteracoes_12_meses=iteracoes_12_meses,
        meses_inativo_12_meses=meses_inativo_12_meses,
        limite_de_credito=limite_de_credito,
        valor_transacoes_12_meses=valor_transacoes_12_meses,
        qtd_transacoes_12_meses=qtd_transacoes_12_meses,
        predicao_credito=predicao_credito
    )
    logger.debug("Adicionando cliente de nome: '%s'", cliente.nome_cliente)

    try:
        # Criando conexão com a base
        session = Session()
        
        # Checando se cliente já existe na base
        if session.query(Cliente).filter(Cliente.nome_cliente == form.nome_cliente).first():
            error_msg = "Cliente já existente na base :/"
            logger.warning("Erro ao adicionar cliente '%s', %s", cliente.nome_cliente, error_msg)
            return {"message": error_msg}, 409
        
        # Adicionando cliente
        session.add(cliente)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug("Adicionado cliente de nome: '%s'", cliente.nome_cliente)
        return apresenta_cliente(cliente), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo cliente :/"
        logger.warning("Erro ao adicionar cliente '%s', %s", cliente.nome_cliente, error_msg)
        return {"message": error_msg}, 400

# Métodos baseados em nome
# Rota de busca de cliente por nome
@app.get('/cliente', tags=[cliente_tag],
         responses={"200": ClienteViewSchema, "404": ErrorSchema})

def get_cliente(query: ClienteBuscaSchema):    
    """Faz a busca por um cliente cadastrado na base a partir do nome

    Args:
        nome_cliente (str): nome do cliente
        
    Returns:
        predicaoCredito: representação do diagnóstico de credito associado ao cliente
    """
    
    cliente_nome_cliente = query.nome_cliente
    logger.debug("Adicionado cliente de nome: '%s'", cliente_nome_cliente)
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    cliente = session.query(Cliente).filter(Cliente.nome_cliente == cliente_nome_cliente).first()

    if not cliente:
        # se o cliente não foi encontrado
        error_msg = f"Cliente {cliente_nome_cliente} não encontrado na base :/"
        logger.warning("Erro ao buscar cliente '%s', %s", cliente_nome_cliente, error_msg)
        return {"message": error_msg}, 404
    else:
        logger.debug("Cliente encontrado: '%s'", cliente.nome_cliente)
        # retorna a representação do cliente
        return apresenta_cliente(cliente), 200


# Rota de remoção de cliente por nome
@app.delete('/cliente', tags=[cliente_tag],
            responses={"200": ClienteViewSchema, "404": ErrorSchema})
def delete_cliente(query: ClienteBuscaSchema):
    """Remove um cliente cadastrado na base a partir do nome

    Args:
        nome_cliente (str): nome do cliente
        
    Returns:
        msg: Mensagem de sucesso ou erro
    """
    
    cliente_nome_cliente = unquote(query.nome_cliente)
    logger.debug("Deletando dados do cliente: '%s'", cliente_nome_cliente)
    
    # Criando conexão com a base
    session = Session()
    
    # Buscando cliente
    cliente = session.query(Cliente).filter(Cliente.nome_cliente == cliente_nome_cliente).first()
    
    if not cliente:
        error_msg = "Cliente não encontrado na base :/"
        logger.warning("Erro ao buscar cliente '%s', %s", cliente_nome_cliente, error_msg)
        return {"message": error_msg}, 404
    else:
        session.delete(cliente)
        session.commit()
        logger.debug("Deletado cliente '%s'", cliente_nome_cliente)
        return {"message": f"Cliente {cliente_nome_cliente} removido com sucesso!"}, 200
    
if __name__ == '__main__':
    app.run(debug=True)