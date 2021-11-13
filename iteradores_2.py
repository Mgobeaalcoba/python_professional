"""
Con un iterador puedo guardar secuencias matematicas infinitas sin 
usar importante espacio en memoria de mi CPU. Ya que los voy generando
en la medida que los voy necesitando. Ej: todos lo numeros pares o
la sucesión de fibonacci.

Para crear un iterador debo crear clases o class y para profundizar
en ello debo tomar el curso de programación orientada a objetos
"""
import time

class FiboIter():

    def __iter__(self): 
        """ 
        Reglas de la programación orientada a objetos en python:
        1- metodo "dander"/"iter": el nombre de la función va precedido y
        continuado por __ (doble guion bajo) y recibe a "self" como parametro
        porque todos los metodos de una clase necesitan este parametro para poder 
        existir
        2- metodo "dander"/"next": tmb recibe a "self" como parametro. 
        Podría tener tmb el metodo "dander"/"init" (__init__): permite 
        inicializar un objeto -> constructor. No es necesario porque no 
        requiere ningún atributo
        """
        self.n1=0
        self.n2=1
        self.counter=0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1 # Primer elemento de la sucesión de Fibonacci: el 0
        elif self.counter == 1:
            self.counter += 1
            return self.n2 # Segundo elemento de la sucesión de Fibonacci: el 1
        else:
            self.aux = self.n1 + self.n2 # Genero un metodo auxiliar para guardar la suma de ambos
            # self.n1 = self.n2
            # self.n2 = self.aux
            self.n1, self.n2 = self.n2, self.aux #Hago Swaping para realizar el intercambio de arriba en una sola linea
            self.counter += 1
            return self.aux

if __name__ == "__main__":
    fibonacci = FiboIter()
    for element in fibonacci:
        print(element)
        time.sleep(0.5)
