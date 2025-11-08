from excecoes import OperacaoInvalidaException
from extrato import Extrato

class Conta:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo
        self.__extrato = Extrato()
        
    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    def _atualizar_saldo(self, novo_saldo):
        self.__saldo = novo_saldo
    
    def depositar(self, valor):
        if valor <= 0:
            raise OperacaoInvalidaException("O valor do deposito deve ser maior que zero.")
        self.__saldo += valor
        self.__extrato.adicionar_transacao(f"Deposito: R${valor:.2f}")
        print(f"Deposito de R${valor:.2f} realizado")
        
    def sacar(self, valor):
        try:
            if valor > self.__saldo:
                raise OperacaoInvalidaException("Saldo insuficiente para saque")
            if valor <= 0:
                raise OperacaoInvalidaException("O valor do saque deve ser maior que 0")
            self.__saldo -= valor
            self.__extrato.adicionar_transacao(f"Saque: R${valor:.2f}")
            print("Saque realizado com sucesso")
                
        except OperacaoInvalidaException as e:
            print(f"Erro: {e}") 
            
    def exibir_extrato(self):
        print(f"\nExtrato de {self.__titular}")
        self.__extrato.exibir()
        print(f"Saldo atual: R${self.__saldo:.2f}")
    
    def __str__(self):
        return f"Saldo atual de {self.__titular}: R${self.__saldo:.2f}"