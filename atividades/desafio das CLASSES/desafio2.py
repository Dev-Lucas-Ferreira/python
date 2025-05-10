class Triangulo:
    def __init__(self, base,altura):
        self.base = base
        self.altura = altura

    def area(self):
        calculo = (self.base * self.altura)/2
        print(f"A área do triangulo é {calculo}")

triangulo = Triangulo(86,50)
triangulo.area()

        