from typing import List

# Creando un iterador

my_list: List[int] = [1,2,3,4,5]
my_iter = iter(my_list) # Creo un objeto "iterador" con la funcion iter

# Iterando un iterador

# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

# Para no repetir todas las lineas de codigo por cada valor del iterable debo hacer: 

while True: #Ciclo While Infinito, solo se sale con un break
    try: # Uso manejo de errores para romper el while cuando se presente el error "StopIteration"
        element = next(my_iter) # Recorro mi objeto iterador con la building function next
        print(element)
    except StopIteration:
        break

# Bien: Este ciclo While infinito se puede simplificar mediante
# sugar sintax con un ciclo for. El ciclo for, como tal no existe en 
# python sino que es en realidad un ciclo while infinito con manejo
# de errores que corta cuando termina de recorrer un iterable, es 
# decir, cuando se presentá el error "StopIteration"

for element in my_list:
    print(element)

# Obtengo el mismo resultado con el ciclo for. 

# Cuando no quedan datos, la excepción StopIteration es elevada. 

# Castear: Convertir un iterable en un iterador
