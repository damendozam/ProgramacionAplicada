from __future__ import print_function
from ast import Return
from typing_extensions import Self


class Animal(object):
    habitat=""
    alimentacion=""
    def __init__(self,nombre,especie,peso,color):
        self.nombre=nombre
        self.especie=especie
        self.peso=peso
        self.color=color
    def comunicacion(self):
        print("el animal se comunica")
        
    def desplazamiento(self,desplazamiento):
        self.desplazamiento = desplazamiento
    def alimentacion(self,alimentacion):
        self.alimentacion = alimentacion
    def habitat(self, habitat):
        self.habitat = habitat

class Raza(object):
    def __init__(self):
         pass
    def begin(self,pitbull,labrador,dalmata):
        self.pitbull = pitbull
        self.labrador = labrador
        self.dalmata = dalmata
         

class Textura(object):
    def __init__(self):
        pass
    def begin(self,escamas,manchas, rayas, melenuda):
        self.escamas = escamas
        self.manchas = manchas
        self.rayas = rayas


class pez(Animal):

    textura=Textura()
    raza= Raza() 
    def __init__(self, nombre, especie, peso, color):
        self.nombre =nombre
        self.color= color
        self.especie = especie
        self.peso =peso
class perro(Animal,Raza):
     def __init__(self, nombre, especie, peso, color):
         self.color=color
         self.nombre=nombre
         self.especie=especie
         self.peso=peso
         
def getNombre(self):
    return self.nombre
def getEspecie(self):
    return self.especie
def getPeso(self):
    return self.peso
def getColor(self):
    return self.color

def mostrarAnimal(self):
    print("\nnombre: "+self.getNombre()+"\nespecie: "+self.getEspecie()+"\npeso: "+self.getPeso()+"\ncolor: "+self.getColor())

         

          
                    
 

    

  