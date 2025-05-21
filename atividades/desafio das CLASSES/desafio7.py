class Retangulo:
   def __init__(self, base, altura):
       self.base = base
       self.altura = altura


   def area(self):
       area = self.base * self.altura 
       print(f"Essa é a area {area}") 


   def perimetro(self):
       perimetro = 2 * (self.base + self.altura)
       print(f"Esse é o perimetro {perimetro}")


retangulo = Retangulo(86,97)
retangulo.area()
retangulo.perimetro()   