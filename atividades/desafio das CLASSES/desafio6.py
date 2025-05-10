class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        # Inicia a conta com um saldo inicial
        self.saldo = saldo_inicial
    
    def depositar_dinheiro(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"R${valor} foi depositado com sucesso. Saldo atual: R${self.saldo}")
        else:
            print("Não é possível depositar esse valor.")

    def sacar_dinheiro(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Parabéns pelo saque de R${valor}. Saldo atual: R${self.saldo}")
        elif valor > self.saldo:
            print("Saldo insuficiente para saque.")
        else:
            print("Não é possível sacar esse valor.")


conta = ContaBancaria(100)  
conta.depositar_dinheiro(50)  
conta.sacar_dinheiro(30)      
conta.sacar_dinheiro(200)     
