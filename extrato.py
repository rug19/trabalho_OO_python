class Extrato:
    def __init__(self):
        self.__transacoes = []
        
    def adicionar_transacao(self, descricao):
        self.__transacoes.append(descricao)
    
    def exibir(self):
        print("\n--EXTRATO--")
        if not self.__transacoes:
            print("Nenhuma transacao realizada.")
        else:
            for transacao in self.__transacoes:
                print(transacao)
        print("--------------")