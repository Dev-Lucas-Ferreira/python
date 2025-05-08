from modulo import *

def calculos():
        limpar_tela()
        print("╔═════════[Calculo]═════════╗")
        print("║           Área            ║")
        print("║═══════════════════════════║")
        print("║     1 - Retangulo         ║")
        print("║     2 - Quadrado          ║")
        print("║     3 - Triangulo         ║")
        print("║     4 - Circulo           ║")
        print("╚═══════════════════════════╝")
        escolha = input("Qual calculo a escolher?")
        if escolha.lower() in ["retangulo","1"]:
                limpar_tela()
                calc_area_retangulo()
        elif escolha.lower() in ["quadrado","2"]:
                limpar_tela()
                calc_area_quadrado()
        elif escolha.lower() in ["triangulo","3"]:
                limpar_tela()
                calc_area_triangulo
        elif escolha.lower() in ["Circulo","4"]:
                limpar_tela()
                calc_area_circulo()

calculos()