from typing import List
import json
from pydantic import BaseModel
import numpy as np
from model.cliente import Cliente



class ClienteSchema(BaseModel):
    """ Define como um novo cliente a ser inserido deve ser representado
    """
    nome_cliente:str = "Fulano de tal"
    idade: int = 21
    sexo: int = 1
    dependentes: int = 1
    escolaridade: int = 0
    estado_civil: int = 2
    salario_anual: int = 0
    tipo_cartao: int = 0
    meses_de_relacionamento: int = 60
    qtd_produtos: int = 5
    iteracoes_12_meses: int = 18
    meses_inativo_12_meses: int = 1
    limite_de_credito: int = 30000.00
    valor_transacoes_12_meses: float = 65000.00
    qtd_transacoes_12_meses: int = 24
    
class ClienteViewSchema(BaseModel):
    """Define como o cliente será retornado
    """
    id: int = 1
    nome_cliente: str = "Fulano de tal"
    idade: int = 20
    sexo: int = 1
    dependentes: int = 1
    escolaridade: int = 2
    estado_civil: int = 1
    salario_anual: int = 0
    tipo_cartao: int = 0
    meses_de_relacionamento: int = 60
    qtd_produtos: int = 5
    iteracoes_12_meses: int = 18
    meses_inativo_12_meses: int = 1
    limite_de_credito: int = 30000.00
    valor_transacoes_12_meses: float = 65000.00
    qtd_transacoes_12_meses: int = 24
    predicao_credito: int = 0
       
class ClienteBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do cliente.
    """
    nome_cliente: str = "Marialdo"

class ListaClientesSchema(BaseModel):
    """Define como uma lista de clientes será representada
    """
    clientes: List[ClienteSchema]
      
class ClienteDelSchema(BaseModel):
    """Define como o cliente para deleção será representado
    """
    nome_cliente: str = "Marialdo"
    
# Apresenta apenas os dados de um cliente
def apresenta_cliente(cliente: Cliente):
    """ Retorna uma representação do cliente seguindo o schema definido em
        ClienteViewSchema.
    """
    return {
            "id": cliente.id,
            "nome_cliente": cliente.nome_cliente,
            "idade": cliente.idade,
            "sexo": cliente.sexo,
            "dependentes": cliente.dependentes, 
            "escolaridade": cliente.escolaridade,
            "estado_civil": cliente.estado_civil,
            "salario_anual": cliente.salario_anual,
            "tipo_cartao": cliente.tipo_cartao,
            "meses_de_relacionamento": cliente.meses_de_relacionamento,
            "qtd_produtos": cliente.qtd_produtos,
            "iteracoes_12_meses": cliente.iteracoes_12_meses,
            "meses_inativo_12_meses": cliente.meses_inativo_12_meses,
            "limite_de_credito": cliente.limite_de_credito,
            "valor_transacoes_12_meses": cliente.valor_transacoes_12_meses,
            "qtd_transacoes_12_meses": cliente.qtd_transacoes_12_meses,
            "predicao_credito": cliente.predicao_credito
        }
        
# Apresenta uma lista de clientes
def apresenta_clientes(clientes: List[Cliente]):
    """ Retorna uma representação do cliente seguindo o schema definido em
        ClienteViewSchema.
    """
    result = []
    for cliente in clientes:
        result.append({
        "id": cliente.id,
        "nome_cliente": cliente.nome_cliente,
        "idade": cliente.idade,
        "sexo": cliente.sexo,
        "dependentes": cliente.dependentes,
        "escolaridade": cliente.escolaridade,
        "estado_civil": cliente.estado_civil,
        "salario_anual": cliente.salario_anual,
        "tipo_cartao": cliente.tipo_cartao,
        "meses_de_relacionamento": cliente.meses_de_relacionamento,
        "qtd_produtos": cliente.qtd_produtos,
        "iteracoes_12_meses": cliente.iteracoes_12_meses,
        "meses_inativo_12_meses": cliente.meses_inativo_12_meses,
        "limite_de_credito": cliente.limite_de_credito,
        "valor_transacoes_12_meses": cliente.valor_transacoes_12_meses,
        "qtd_transacoes_12_meses": cliente.qtd_transacoes_12_meses,        
        "predicao_credito": cliente.predicao_credito
        })
    return {"clientes": result}