import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def area_circulo(self):
        area = math.pi * (self.raio ** 2)
        print(f"A área é de {area}")
    
    def circunferencia(self):
        circunferencia = 2 * math.pi * self.raio
        print(f"A circunferência é {circunferencia}")


circulo = Circulo(85)
circulo.area_circulo() 
circulo.circunferencia()  
