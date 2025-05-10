class Cachorro:
   def __init__(self, latir):
       self.latir = latir
  
   def latido(self):
       print(self.latir)


cachorro = Cachorro('AUAU')
cachorro.latido()