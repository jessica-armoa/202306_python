class Usuario:		# esto es lo que tenemos hasta ahora
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.balance_cuenta = 0

  def hacer_deposito(self, amount):	# toma un argumento que es el monto del depósito
    self.balance_cuenta += amount	# la cuenta del usuario específico aumenta en la cantidad del valor recibido

  def hacer_retiro(self, amount):
    self.balance_cuenta -= amount

  def mostrar_balance_usuario(self):
    print(self.name+", Balance:"+str(self.balance_cuenta))

  def transferir_dinero(self, other_user, amount):
    self.hacer_retiro(amount)
    other_user.hacer_deposito(amount)

guido = Usuario("Guido", "guido@gmail.com")
jessica = Usuario("Jessica", "jessica@gmail.com")
andrea = Usuario("Andrea", "andrea@gmail.com")


guido.hacer_deposito(500)
guido.hacer_deposito(300)
guido.hacer_deposito(100)
guido.hacer_retiro(200)
guido.mostrar_balance_usuario()

jessica.hacer_deposito(500)
jessica.hacer_deposito(300)
jessica.hacer_retiro(500)
jessica.hacer_retiro(50)
jessica.mostrar_balance_usuario()

andrea.hacer_deposito(500)
andrea.hacer_retiro(50)
andrea.hacer_retiro(50)
andrea.hacer_retiro(50)
andrea.mostrar_balance_usuario()

guido.transferir_dinero(andrea, 500)
guido.mostrar_balance_usuario()
andrea.mostrar_balance_usuario()