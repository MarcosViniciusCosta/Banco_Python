saldo = 0
saquesDiariosRestantes = 3
log = ""

def mostrarMenu():
    print("\nDigite o valor 1 para verificar o extrato")
    print("Digite o valor 2 para realizar um saque")
    print("Digite o valor 3 para realizar um depósito")
    print("Digite o valor 0 para sair do sistema")

def realizarDeposito(valorDepositado):
    valorDepositadoEhPositivo = (valorDepositado >=0)
    if valorDepositadoEhPositivo:
        global saldo 
        saldo += valorDepositado
        registrarLog(f"Realizado depósito de R$ {valorDepositado:.2f} ")

def realizarSaque(valorSacado):
    global saldo
    global saquesDiariosRestantes
    
    valorSacadoEhPositivo = (valorSacado>= 0)
    valorSacadoEstaDentroDoLimite = (valorSacado <=500)
    valorSacadoDeixaSaldoPositivo = (valorSacado <= saldo)
    aindaHaSaquesDiariosDisponiveis = (saquesDiariosRestantes > 0)
    
    if(valorSacadoEhPositivo and valorSacadoEstaDentroDoLimite 
       and valorSacadoDeixaSaldoPositivo and aindaHaSaquesDiariosDisponiveis):
        
                saldo -= valorSacado
                registrarLog(f"Realizado saque de R$ {valorSacado:.2f} ")
                saquesDiariosRestantes -= 1

    else:
        print("Impossível sacar o dinheiro por falta de saldo ou excesso de saques diários")
       

def tratarOpcaoEscolhida(opcaoEscolhida):
    global saldo
    if opcaoEscolhida == "1":
        exibirExtrato()    
    elif opcaoEscolhida == "2":
        valorSacado =  input("Digite o valor a ser sacado: ")
        realizarSaque(float(valorSacado))
    elif opcaoEscolhida == "3":
        valorDepositado = input("Digite o valor a ser depositado: ")
        realizarDeposito(float(valorDepositado))    
    elif(opcaoEscolhida == "0"):
        print ("saindo ...")
    else:
        print("Opção inválida, tente novamente!")    


def registrarLog(mensagem):
    global log
    log += (mensagem+"\n")
 
def exibirExtrato():
    global log
    print(f"\n{log}Saldo atual: R$ {saldo:.2f} \n")
  
opcao = 482

while opcao != "0":
    mostrarMenu()
    opcao = input("Valor: ")
    tratarOpcaoEscolhida(opcao)
