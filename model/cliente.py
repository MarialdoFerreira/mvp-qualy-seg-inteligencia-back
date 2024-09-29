from datetime import datetime
from typing import Union
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, DateTime, Float
from  model import Base

class Cliente(Base):
    __tablename__ = 'clientes'
    
    id = Column(Integer, primary_key=True)
    nome_cliente = Column('Nome do Cliente', String(50))
    idade = Column('Idade', Integer)
    sexo = Column('Gênero', Integer)
    dependentes = Column('Dependentes', Integer)
    escolaridade = Column('Escolaridade', Integer)
    estado_civil = Column('Estado Civil', Integer)
    salario_anual = Column('Salario Anual', Integer)
    tipo_cartao = Column('Tipo de Cartao', Integer)
    meses_de_relacionamento = Column('Meses de Relacionamento', Integer)
    qtd_produtos = Column('Qtd de Produtos', Integer)
    iteracoes_12_meses = Column('Iteracoes em 12 meses', Integer)
    meses_inativo_12_meses = Column('Meses Inativos em 12 meses', Integer)
    limite_de_credito = Column('Limite de credito', Float)
    valor_transacoes_12_meses = Column('Valor das Transacoes em 12 meses', Float)
    qtd_transacoes_12_meses = Column('Qtd de Transacoes em 12 meses', Integer)
    predicao_credito = Column('Predicao de Credito', Integer)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__ (self, nome_cliente:str, idade:int, sexo:int, dependentes:int,
                 escolaridade:int, estado_civil:int, salario_anual:int, tipo_cartao:int,
                 meses_de_relacionamento:int, qtd_produtos:int, iteracoes_12_meses:int,
                 meses_inativo_12_meses:int, limite_de_credito:float, valor_transacoes_12_meses:float,
                 qtd_transacoes_12_meses:int, predicao_credito:int, data_insercao:Union[DateTime, None] = None):
        """
        Cria um Cliente

        Arguments:
            nome:                       nome do cliente
            idade:                      idade
            sexo:                       sexo
            dependentes:                dependentes
            escolaridade:               escolaridade
            estado_civil:                estado Civil
            salario_anual:               salario Anual
            tipo_cartao:                 tipo de Cartao
            meses_de_relacionamento:        meses de Relacionamento
            qtd_produtos:                qtd de Produtos do cliente no banco
            iteracoes_12_meses:         iteracoes do cliente em 12 meses
            meses_inativo_12_meses:      meses Inativo do cliente em 12 meses
            limite_de_credito:          limite de credito
            valor_transacoes_12_meses:   valor Transacoes em 12 meses
            qtd_transacoes_12_meses:     qtd de transacoes em 12 meses
            predicaoCredito:            diagnostico da analise de credito do cliente Adimplir(0) ou inadimplir(1)
            data_insercao:              data de quando o cliente foi inserido à base
        """
        self.nome_cliente = nome_cliente
        self.idade = idade
        self.sexo = sexo
        self.dependentes = dependentes
        self.escolaridade = escolaridade
        self.estado_civil = estado_civil
        self.salario_anual = salario_anual
        self.tipo_cartao = tipo_cartao
        self.meses_de_relacionamento = meses_de_relacionamento
        self.qtd_produtos = qtd_produtos
        self.iteracoes_12_meses = iteracoes_12_meses
        self.meses_inativo_12_meses = meses_inativo_12_meses
        self.limite_de_credito = limite_de_credito
        self.valor_transacoes_12_meses = valor_transacoes_12_meses
        self.qtd_transacoes_12_meses = qtd_transacoes_12_meses
        self.predicao_credito = predicao_credito
        
        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao