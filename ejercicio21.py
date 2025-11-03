class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, cantidad):
        self.saldo = self.saldo + cantidad
        print (f"Deposito exitoso, tu nuevo saldo es {self.saldo}")
        
    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo = self.saldo - cantidad
            print (f"Retiro exitoso! Saldo restante: {self.saldo}")
        else:
            print("Error: Fondos insuficientes")


mi_cuenta = CuentaBancaria("Juan Perez", 1000)

mi_cuenta.depositar(500) # Debería mostrar 1500
mi_cuenta.retirar(200)   # Debería mostrar 1300
mi_cuenta.retirar(1500)  # Debería mostrar "Fondos insuficientes"
