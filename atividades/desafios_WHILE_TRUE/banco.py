import os

# Variáveis globais
nome = ""
saldo = 0.0

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def criar_conta():
    global nome, saldo
    limpar_tela()
    print("==========[ CRIAR CONTA ]==========")
    nome = input("Digite seu nome: ").strip().title()
    try:
        saldo = float(input("Valor do primeiro depósito: R$ "))
        if saldo <= 0:
            print("Valor inválido! O depósito inicial deve ser maior que R$0.")
            return
    except ValueError:
        print("Por favor, digite um valor numérico válido.")
        return

    confirmar = input("Confirmar criação da conta? (s/n): ").lower()
    if confirmar in ["s", "sim"]:
        print(f"\nConta criada com sucesso para {nome}!")
        input("Pressione ENTER para continuar...")
        limpar_tela()
        menu_banco()
    else:
        print("Criação da conta cancelada.")

def saque():
    global saldo
    limpar_tela()
    print("=========== [ SAQUE ] ===========")
    print(f"Saldo atual: R$ {saldo:.2f}")
    try:
        valor = float(input("Digite o valor do saque: R$ "))
        if valor <= 0:
            print("O valor deve ser maior que R$0.")
        elif valor > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            print(f"Novo saldo: R$ {saldo:.2f}")
    except ValueError:
        print("Entrada inválida. Digite um número.")
    input("\nPressione ENTER para voltar ao menu...")

def deposito():
    global saldo
    limpar_tela()
    print("========= [ DEPÓSITO ] =========")
    print(f"Saldo atual: R$ {saldo:.2f}")
    try:
        valor = float(input("Digite o valor do depósito: R$ "))
        if valor <= 0:
            print("O valor deve ser maior que R$0.")
        else:
            saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            print(f"Novo saldo: R$ {saldo:.2f}")
    except ValueError:
        print("Entrada inválida. Digite um número.")
    input("\nPressione ENTER para voltar ao menu...")

def menu_banco():
    while True:
        limpar_tela()
        print("======= [ BANCO GUIANA BRASILEIRA ] =======")
        print(f"Cliente: {nome}")
        print(f"Saldo: R$ {saldo:.2f}")
        print("-------------------------------------------")
        print("1 - Sacar")
        print("2 - Depositar")
        print("3 - Consultar Saldo")
        print("4 - Sair")
        print("===========================================")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            saque()
        elif opcao == '2':
            deposito()
        elif opcao == '3':
            print(f"\nSeu saldo atual é: R$ {saldo:.2f}")
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == '4':
            print("\nObrigado por usar o Banco Guiana Brasileira!")
            break
        else:
            print("Opção inválida!")
            input("Pressione ENTER para tentar novamente...")

# Início do programa
criar_conta()
