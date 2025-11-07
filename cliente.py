class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__contas = []
        

    
    def adicionar_conta(self, conta):
        self.__contas.append(conta)
        
    def listar_contas(self):
        print(f"\nContas do cliente {self.__nome}:")
        for conta in self.__contas:
            print(f"{conta}")