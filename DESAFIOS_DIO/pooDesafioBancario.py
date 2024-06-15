from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class cliente:
    def __init__(self,endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta,transacao):
        transacao.registrar(conta)

    def adicionar_conta(self,conta):
        self.conta.append(conta)

class Pessoa(cliente):
    def __init__(self,nome,data_nasc, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nasc = data_nasc
        self.cpf = cpf

class conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0010'
        self._cliente = cliente
        self._historico = historico()
    
    @classmethod
    def nova_conta(cls,cliente,numero):
        return cls(numero,cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self,valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print('\n :( infelizmente sua operação falhou! você não tem saldo')
        elif valor > 0:
            self._saldo -= valor
            print('\n ʚɞ ⁺˖ ⸝⸝ seu saque foi realizado yeyy!!')
            return True
        else: 
            print('\n operação nao realizada ㅤ/ᐠ - ˕ -マ valor invalido')

        return False
    
    def depositar(self,valor):
        if valor > 0:
            self._saldo += valor
            print('\n 𓆩♡𓆪 Seu depósito foi realizado!!')
        else:
            print('\n oh não! a operação falhou, valor inserido é invalido')
            return False
        return True

class ContaCorrente(conta):
    def __init__(self, numero, cliente, limite=1000, limite_saque=5):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque

    def sacar (self, valor):
        numero_saques = len (
            [transacao for transacao in self.historico.transacoes if transacao ['tipo'] == saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print('\n poxa vida! seu saque excede o valor limite!')

        elif excedeu_saques:
            print('n ops! você excedeu o valor limite de saques!')
        
        else:
            return super().sacar(valor)
        return False
    
    def __str__(self):
        return f'''\
            agencia: \t{self.agencia}
            CC: \t\t{self.numero}
            titular: \{self.cliente.nome}
        '''
    
class historico:
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adc_transacao(self,transacao):
        self.transacao.append(
            {
                'tipo' : transacao.__class__.name__,
                'valor' : transacao.valor
            }
        )

class transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    @abstractclassmethod
    def registrar(self,conta):
        pass

class saque(transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adc_transacao(self)

class deposito(transacao):
    def __init__(self,valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adc_transacao(self)

