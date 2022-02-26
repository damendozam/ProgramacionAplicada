from json.tool import main
from os import name
from typing_extensions import Self
from animals import Animal 
from animals import Raza
from animals import perro
from animals import Textura
from animals import pez

if __name__ == "main" :
    print ("Animal")
Animal1=Animal ("rex","tiburon","15gramos","azul")
print (Animal1)
listatest=[Animal1]

def  __str__(self):
        return "{}, nombre: {}, especie: {} , {} peso {} color ".format(type(self).__name__,self.nombre,self.especie,Self.color,
    )
    
def __repr__(self):
        return self.__str__()


Animal2=perro ("murdoc","gramde","150kilogramos","maron")
print(Animal1)
listatest = [Animal2]
animal3=Textura (perro)
Animal4= pez ("nemo","grande","1202","naranja")
print (Animal4)
listatest =[Animal4]

if __name__ == "main" :
    print ("Animal")

    













