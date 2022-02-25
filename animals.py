from __future__ import print_function
from ast import Return
from typing_extensions import Self


class Animal(object):
    def __init__(self,nombre,especie,peso,color):
        self.nombre=nombre
        self.especie=especie
        self.peso=peso
        self.color=color       
    def comunicacion(self,comunicacion):
        self.comunicacion = comunicacion       
    def desplazamiento(self,desplazamiento):
        self.desplazamiento = desplazamiento
    def alimentacion(self,alimentacion):
        self.alimentacion = alimentacion
    def habitat(self, habitat):
        self.habitat = habitat

class Raza():
    def __init__(self):
         pass
    def begin(self,pitbull,labrador,dalmata):
        self.pitbull = pitbull
        self.labrador = labrador
        self.dalmata = dalmata
         

class Textura():
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
     def __init__(self, nombre, raza, peso, color):
         self.color=color
         self.nombre=nombre
         self.raza =raza
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

         
nombre = raw_input("Ingrese el nombre: ")
especie = raw_input("Ingrese que tipo de especie es el animal: ")
peso = raw_input("Ingrese el peso del animal: ")
color = raw_input("Describa el color del animal: ")

a =Animal(nombre,especie,peso,color)
a.mostrarAnimal()

perro1 = Perro("Firulais","pitbull","20kg","blanco con cafe")
perro2 = Perro("Mateo","labrador","30kg","amarillo")
perro3 = Perro("Toby","Bulldog","24kg","Blanco")

pez1 = Pez("Nemo","pez dorado","0,5kg","amarillento-anaranjado")
pez2 = Pez("Pez betta","pez betta cola de rosa","0.8kg","rosado y blanco" )
pez3 = Pez("Apolo","guppy","10gramos","azul y blanco")

print("Mi nombre es",perro1.nombre,"mi raza es",perro1.raza,"mi peso es de",perro1.peso,"soy de color",perro1.color)
print("Mi nombre es",perro2.nombre,"mi raza es",perro2.raza,"mi peso es de",perro2.peso,"soy de color",perro2.color)
print("Mi nombre es",perro3.nombre,"mi raza es",perro3.raza,"mi peso es de",perro3.peso,"soy de color",perro3.color)

print("Mi nombre es",pez1.nombre,"mi especie es",pez1.especie,"mi peso es de",pez1.peso,"soy de color",pez1.color)
print("Mi nombre es",pez2.nombre,"mi especie es",pez2.especie,"mi peso es de",pez2.peso,"soy de color",pez2.color)   
print("Mi nombre es",pez3.nombre,"mi especie es",pez3.especie,"mi peso es de",pez3.peso,"soy de color",pez.color)                  
 

    

  