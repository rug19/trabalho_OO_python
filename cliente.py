class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__contas = []
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf

    
    def adicionar_conta(self, conta):
        self.__contas.append(conta)
        
    def listar_contas(self):
        tipos_contas = [type(conta).__name__ for conta in self.__contas]

        print("\n" + "="*30)
        print(f"CLIENTE: {self.__nome}")
        print(f"CPF: {self.__cpf}")
        print(f"CONTAS VINCULADAS: {', '.join(tipos_contas) if tipos_contas else 'Nenhuma'}")
        print("\n" + "="*30)
        
        