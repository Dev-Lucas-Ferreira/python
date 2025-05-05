from jogo_numero_secreto import *

#Funçoes do banco


def criar_conta():
    print("=========================")
    nome = input("Qual o nome do Usúario:")
    dinheiro = float(input("Qual vai ser o  valor do primeiro deposito:"))
    acao = input("Confirmar?(s/n)")

    while True:
        try:
            if dinheiro <= 0:
                print("O valor minimo e de 1 real")
                return
            elif acao.lower() == ["s","sim"]:
                limpar_tela()
                menu


    print("=========================")

def saque():
    print("====================[Saque]======================")
    print(f"Saldo:{}")
    print("=================================================")

    valor = int(input("Quanto você vai sacar?"))


def deposito():
    print("===================[Deposito]====================")
    print(f"Saldo:{}")
    print("=================================================")

    valor = float(input("Quanto você vai depositar?"))
    

def Banco_menu(acao):
    print("=========[Bem vindo a guiana brasileira]=========")

    print(f"Nome:{}")
    print(f"Saldo:")

    print("1<[SAQUE]                            [DEPOSITO]>2")

    print("=================================================")

    acao = input("O que deseja fazer?")



