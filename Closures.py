# Un Closure se da cuando una variable de un scope superior es recordada. 
# Y aunque se elimine ese scope superior yo puedo seguir accediendo a una variable
# eliminada. 

# reglas para encontrar un closure

# debemos tener una nested function
# la nested function debe referenciar un valor de un scope superior
# la función que envuelve la nested debe retornar a esta función

# Las tres se cumplen en el siguiente ejemplo:

def main():

    a = 1

    def nested():
        print(a)

    return nested

my_func = main()
my_func()

del(main)

my_func()