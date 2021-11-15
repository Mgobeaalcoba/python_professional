"""
Colección desordenada de elementos unicos e inmutables.
no puede contener listas o diccionarios que son elementos
mutables. Tmp puede contener elementos que se repitan. 
"""
my_set = {3, 4, 5}
print("my set =", my_set)

my_set2 = {"Hola", 23.3, False, True}
print("my set2 =", my_set2)

my_set3 = {3, 3, 2}
print("my set3 =", my_set3)

# my_set4 = {[1, 2, 3], 4} # Va a arrojar error porque una lista es mutable
# print("my set4 =", my_set4)

# Como armar un set vacio: 

empty_set = {} # Arma un diccionario vacio
print(type(empty_set))

empty_set2 = set() # Arma un set vacio
print(type(empty_set2))

# Casting con sets

my_list = [1,1,2,3,4,4,5]
my_set = set(my_list)
print(my_set)

my_tuple = ("Hola", "Hola", "Hola", 1)
my_set2 = set(my_tuple)
print(my_set2)

# Añadir elementos a un set:

my_set = {1,2,3}
print(my_set)

# Añadir un elemento
my_set.add(4)
print(my_set) # Imprime {1,2,3,4}

# Añadir multiples elementos
my_set.update([1,2,3]) 
print(my_set) # Imprime {1,2,3,4,5}

# Añadir multiples elementos
my_set.update((1,2,3),{6,8}) 
print(my_set) # Imprime {1,2,3,4,5,6,7,8}

# Borrar elementos de un set
my_set = {1,2,3,4,5,6,7}
print(my_set)

#Borrar un elemento existente
my_set.discard(1)
print(my_set) # Imprime {2,3,4,5,6,7,8}

#Borrar un elemento existente
my_set.remove(2)
print(my_set) # Imprime {3,4,5,6,7,8}

#Borrar un elemento inexistente
my_set.discard(10) 
print(my_set) # Imprime {3,4,5,6,7,8}

#Borrar un elemento inexistente
# my_set.remove(12)
# print(my_set) # Arroja un Key Error porque el valor no existe en el set.

