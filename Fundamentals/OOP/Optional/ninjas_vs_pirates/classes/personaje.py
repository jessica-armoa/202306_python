import random

class Personaje:

    def __init__( self , name , speed):
        self.name = name
        self.strength = (5,15)
        self.speed = speed
        self.health = 100

    def show_stats( self , codigo_color):
        print(chr(27)+"[1;"+codigo_color+"m"+f"Name: {self.name}\nHealth: |"+"|"*(self.health//2)+"-"*((100-self.speed)//2)+"|\n")

    def attack ( self , objetivo , codigo_color):
        print(chr(27)+"[1;"+codigo_color+"m"+f"Golpea: {self.name}")
        golpe = random.randint(self.strength[0], self.strength[1])
        if(golpe>objetivo.health):
            objetivo.health = 0
        else:
            objetivo.health -= golpe
        return self