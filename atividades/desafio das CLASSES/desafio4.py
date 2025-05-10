class Carro:
    def __init__(self, ignição):
        self.ignição = ignição

    def ligar_desligar(self):
        if self.ignição == 1:
            print("O carro ligou")
        elif self.ignição == 0:
            print("O carro desligou")

carro = Carro(0)
carro.ligar_desligar()