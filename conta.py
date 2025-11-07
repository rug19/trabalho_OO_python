from excecoes import OperacaoInvalidaException


class Conta:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo
        
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
            raise OperacaoInvalidaException("O valaor do deposito dever ser maior que zero.")
        self.__saldo += valor
        
    def sacar(self, valor):
        try:
            if valor > self.__saldo:
                raise ("Saldo insuficiente para saque")
            if valor <= 0:
                raise OperacaoInvalidaException(" O valor do saque deve ser maior que 0")
            self.__saldo -= valor
            print("Saque realizado com sucesso")
                
        except OperacaoInvalidaException as e:
            print(f"Erro: {e}") 
    
    def mostrar_saldo(self):
        print(f"Saldo atual de {self.__titular}: R${self.__saldo:.2f}")