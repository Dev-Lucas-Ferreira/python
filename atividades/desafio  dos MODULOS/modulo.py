#Modulos de calculo de área

def limpar_tela():
     print("\033[2J\033[H", end='')
     
def calc_area_retangulo():
    print("========[Calculo_De_Área]========")

    altura = float(input("Qual a altura:"))
    base = float(input("Qual a base:"))

    calc = altura*base

    print(f"A área e de:{calc}")

    

def calc_area_quadrado():
    print("========[Calculo_De_Área]========")
    
    lado = float(input("Qual o tamanho do lado:"))

    calc = lado*4

    print(f"A área do quadado é:{calc}")

    

def calc_area_triangulo():
    print("========[Calculo_De_Área]========")

    altura = float(input("Qual a altura:"))
    base = float(input("Qual a base:"))

    calc = (base*altura)/2

    print(f"A área do triangulo é:{calc}")

    

def calc_area_circulo():
    print("========[Calculo_De_Área]========")

    raio = float(input("Qual o raio do circulo:"))
    pi = 3,14
    
    calc = pi*(raio**2)

    print(f"A área do circulo é:{calc}")