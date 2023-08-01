class CuentaBancaria:
  cuentas = []
  def __init__(self, tasa_interés=0.01, balance=0):
    self.tasa_interés = tasa_interés
    self.balance = balance
    CuentaBancaria.cuentas.append(self)

  def depósito(self, amount):
    self.balance += amount
    return self

  def retiro(self, amount):
    self.balance -= amount
    return self

  def mostrar_info_cuenta(self):
    print("Balace: $", self.balance)

  def generar_interés(self):
    if(self.tasa_interés>0):
      self.balance += self.balance * self.tasa_interés
    return self

  @classmethod
  def imprimir_instancias(cls):
    for cuenta in cls.cuentas:
      cuenta.mostrar_info_cuenta()

cuenta1 = CuentaBancaria(0.02, 100)
cuenta2 = CuentaBancaria(balance=10)

cuenta1.depósito(500).depósito(50).depósito(120).retiro(200).generar_interés().mostrar_info_cuenta()

cuenta2.depósito(50).depósito(150).retiro(10).retiro(50).retiro(10).retiro(25).generar_interés().mostrar_info_cuenta()

print()
CuentaBancaria.imprimir_instancias()