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