class Usuario:		# esto es lo que tenemos hasta ahora
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.balance_cuenta = 0

  def hacer_deposito(self, amount):	# toma un argumento que es el monto del depósito
    self.balance_cuenta += amount	# la cuenta del usuario específico aumenta en la cantidad del valor recibido
    return self

  def hacer_retiro(self, amount):
    self.balance_cuenta -= amount
    return self

  def mostrar_balance_usuario(self):
    print(self.name+", Balance:"+str(self.balance_cuenta))
    return self

  def transferir_dinero(self, other_user, amount):
    self.balance_cuenta -= amount
    other_user.balance_cuenta += amount
    return self

guido = Usuario("Guido", "guido@gmail.com")
jessica = Usuario("Jessica", "jessica@gmail.com")
andrea = Usuario("Andrea", "andrea@gmail.com")

guido.hacer_deposito(500).hacer_deposito(300).hacer_deposito(100).hacer_retiro(200).mostrar_balance_usuario()

jessica.hacer_deposito(500).hacer_deposito(300).hacer_retiro(500).hacer_retiro(50).mostrar_balance_usuario()

andrea.hacer_deposito(500).hacer_retiro(50).hacer_retiro(50).hacer_retiro(50).mostrar_balance_usuario()

guido.transferir_dinero(andrea, 500).mostrar_balance_usuario()
andrea.mostrar_balance_usuario()