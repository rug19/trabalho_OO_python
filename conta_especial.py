from conta import Conta
from excecoes import OperacaoInvalidaException


class ContaEspecial(Conta):
    def __init__(self, titular, saldo=0, limite=0.0):
        super().__init__(titular, saldo)
        self.__limite = limite
        
    def mostrar_saldo(self):
        saldo_limite = self.saldo + self.__limite
        print(f"Saldo atual de {self.titular}: R${self.saldo}\n Saldo + Limite R${saldo_limite}")
        
    def sacar(self, valor):
        try:
            saldo_disponivel = self.saldo + self.__limite
            if valor > saldo_disponivel:
                raise OperacaoInvalidaException("Limite de saque excedido.")
            self._atualizar_saldo(self.saldo - valor)
            print(f"Saque de R${valor:.2f} realizado com sucesso (conta especial).")
        except OperacaoInvalidaException as e:
            print(f"Erro: {e}")
        