from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, titular, saldo=0, taxaRendimento=0.0):
        super().__init__(titular, saldo)
        self.__taxaRendimento = taxaRendimento
    
    def render_juros(self):
      rendimento =  self.saldo * self.__taxaRendimento
      self._atualizar_saldo(self.saldo + rendimento)
       
       
        
        
        
        