from classes.ninja import Ninja
from classes.pirate import Pirate

ninja = Ninja("Michelanglo",5)
pirate = Pirate("Jack Sparrow",3)

def sigue_pelea(first, second):
    first.attack(second)
    second.show_stats()

    if(second.health==0):
        return False

    second.attack(first)
    first.show_stats()
    return True

if(ninja.speed>pirate.speed):
    primero = ninja
    segundo = pirate
else:
    primero = pirate
    segundo = ninja

while(primero.health>0 and segundo.health>0):
    sigue = sigue_pelea(primero, segundo)
    if(not sigue):
        break
ganador = primero.name if primero.health > 0 else segundo.name
print(chr(27)+"[1;33m"+f"El ganador es: {ganador}\n\n")





