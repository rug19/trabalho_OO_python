from conta import Conta
from conta_especial import ContaEspecial
from conta_poupanca import ContaPoupanca
from cliente import Cliente

def main():
  cliente1 = Cliente("Ruan", "123.232.123.22")
  
  
  c1 = Conta("Ruan", 1000)
  c2 = ContaEspecial("Ruan", 300, 1000)
  
  cliente1.adicionar_conta(c1)
  cliente1.listar_contas()
    
main()