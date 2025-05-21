from pandas import *
class Itens:
    def __init__(self,data,produto,quantidade,preco):
        self.data = data
        self.produto = produto
        self.quantidade = quantidade
        self.preco = preco
    def dados(self):
        print(self.produto,self.data,self.preco,self.quantidade)

itens = Itens("café","01/01/1001","17,50","5")       