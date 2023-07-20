import math

print("Hola,soy,jessica".split(","))

print("Hola,soy,jessica".find("ola"))

print("1234".isdigit())

print("".join(["Hola","soy"]))

def get_circle_area(r):
  # Return (circunferencia, área) de un círculo de radio r
  c = 2 * math.pi * r
  a = math.pi * r * r
  return (c, a)

circun, area = get_circle_area(20)


dict = {}
lista = [1,2,3,4]
dict = dict.fromkeys(lista, "hola")
print(dict)

#print(str(dict[5]))
print(dict.get(5,"No se encontro"))


capitales = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# otra forma de iterar a través de las claves
for key in capitales:
  print(capitales[key])