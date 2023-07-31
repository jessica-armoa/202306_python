import random
from classes.personaje import Personaje

class Pirate(Personaje):
    pass
"""
    def __init__( self , name ):
        self.name = name
        self.strength = (5,15)
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(chr(27)+"[1;31m"+f"Name: {self.name}\nHealth: |"+"|"*(self.health//2)+"-"*((100-self.speed)//2)+"|\n")

    def attack ( self , ninja ):
        print(chr(27)+"[1;32m"+f"Golpea: {self.name}")
        golpe = random.randint(self.strength[0], self.strength[1])
        if(golpe>ninja.health):
            ninja.health = 0
        else:
            ninja.health -= golpe
        return self
"""
