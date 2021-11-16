# Full Join o union de sets (conjunción de ambos sets)

my_set1 = {3,4,5}
my_set2 = {5,6,7}

my_set3 = my_set1 | my_set2

print(my_set3)

# Inner Join o intersección (Lo que está en ambos sets)

my_set7 = my_set1 & my_set2 # Imprime {5}
print(my_set7)

# Left Join (right join) o diferencia (Lo que está en uno quitandole lo que está en el otro)

my_set4 = my_set1 - my_set2 # Imprime {3,4} 
print(my_set4)

my_set5 = my_set2 - my_set1 # Imprime {6,7}
print(my_set5)

# Diferencia simetrica (contrario de la intersección: me quedo con los elementos que no se comparten en ambos)

my_set6 = my_set1 ^ my_set2 # Imprime {3,4,6,7}
print(my_set6)
