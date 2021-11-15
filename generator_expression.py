"""
Así como yo puedo generar una lista mediante list comprehensión
también puedo armar un generador por comprehension.
¿Como? con la misma sintaxis pero cambiando los corchetes "[]"
por parentesis "()"
"""

# Generator expression

my_list = [0,1,4,7,9,10]

my_second_list = [x*2 for x in my_list] #List comprehension
my_second_gen = (x*2 for x in my_list) # Generator expresssion

print(my_second_list)

# for x in my_second_gen: # Forma abreviada de hacer lo que hago abajo.
#     print(x)

print(next(my_second_gen))
print(next(my_second_gen))
print(next(my_second_gen))
print(next(my_second_gen))
print(next(my_second_gen))
print(next(my_second_gen))

