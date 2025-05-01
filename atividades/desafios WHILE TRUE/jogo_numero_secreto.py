import random
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        limpar_tela()
        print("╔═════════[Jogo]═════════╗")
        print("║     Número Secreto     ║")
        print("║════════════════════════║")
        print("║     1 - Jogar          ║")
        print("║     2 - Regras         ║")
        print("║     3 - Sair           ║")
        print("╚════════════════════════╝")
        escolhas = input("O que desaja fazer?")

        if escolhas.lower() in ["jogar","1"]:
            limpar_tela()
            modos()
        elif escolhas.lower() in ["regras","2"]:
            limpar_tela()
            regras()
        elif escolhas.lower() in ["sair", "3"]:
            break

def regras():
    while True:
        limpar_tela()
        print("╔════════[Regras]════════════╗")
        print("║                            ║")
        print("║  Tente adivinhar o número  ║")
        print("║  que estou pensando!       ║")
        print("║                            ║")
        print("║  Dificuldades:             ║")
        print("║   - Fácil:   1 a 10        ║")
        print("║     Tentativas: 10         ║")
        print("║   - Médio:   1 a 100       ║")
        print("║     Tentativas: 20         ║")
        print("║   - Difícil: 1 a 1000000   ║")
        print("║     Tentativas: 50         ║")
        print("║                            ║")
        print("╚════════════════════════════╝")
        sair = input("Voltar??(s/n)")

        if sair.lower() == "s":
            limpar_tela()
            menu()
        elif sair.lower() == "n":
            limpar_tela()
            regras()

def modos():
    limpar_tela()
    print("╔═════════[Modos]═════════╗")
    print("║        Dificuldade      ║")
    print("║═════════════════════════║")
    print("║  1 - Fácil              ║")
    print("║  2 - Médio              ║")
    print("║  3 - Difícil            ║")
    print("║  4 - Voltar             ║")
    print("╚═════════════════════════╝")
    modo = input("Qual modo gostaria de jogar?")

    if modo.lower() in ["1","facil","fácil"]:
        jogar(1,10,10)
    elif modo.lower() in ["2","medio","médio"]:
        jogar(1,100,20)
    elif modo.lower() in ["3","dificil","dificíl"]:
        jogar(1,1000000,50)
    elif modo.lower() in ["4","voltar"]:
        return
    else:
        print("opção invalida")
        input("Aperte ENTER para continuar")

def jogar(min,max,chances):
    numero = random.randint(min, max)
    chances = chances
    
    while True:
        if chances > 0:
            limpar_tela()
            print(f"╔══════════════════[Chances:{chances}]══════════════════════╗")
            print(f"║ Em qual numero eu estou pensando de {min} a {max}?   ║")
            print("╚════════════════════════════════════════════════════╝")
            try:
                resposta = int(input("Palpite:"))
            except ValueError:
                print("Digite algo valido")
                input()
                continue
        if resposta < numero:
            limpar_tela()
            chances -=1
            print(f"╔═══════════[Chances:{chances}]═══════════╗")
            print(f"║ O número e MAIOR que {resposta}          ║")
            print("╚═════════════════════════════════╝")
            input("Aperte ENTER para continuar")
        elif resposta > numero:
            limpar_tela()
            chances -=1
            print(f"╔═══════════[Chances:{chances}]═══════════╗")
            print(f"║ O número e MENOR que {resposta}         ║")
            print("╚═════════════════════════════════╝")
            input("Aperte ENTER para continuar")
        elif resposta == numero:
            limpar_tela()
            chances -=1
            print(f"╔═══════════[Chances:{chances}]═══════════╗")
            print(f"║ Parábens você acertou 🎉🎉      ║")
            print("╚═════════════════════════════════╝")
            pergunta = input("Deseja jogar de novo??(s/n)")
            break

            if pergunta == "s":
                limpar_tela()
                modos()
            elif pergunta == "n":
                input()
menu()