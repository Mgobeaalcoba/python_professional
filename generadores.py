"""
Los generadores en python son iteradores con una
sintaxis mucho mas simple. Es decir iteradores con 
"sugar syntax"
"""
def my_gen(): # Se inician con una función y no con una clase.
    """ Un ejemplo de generadores """
    
    print("Hello World!")
    n = 0
    yield n # Pausa la función acá y cuando vuelva a entrar va
    # a recorrer desde este yield al proximo. Funciona como un return
    #pero sin necesidad de que vaya al final de la función.

    print("Hello Heaven!")
    n = 1
    yield n

    print("Hello Hell!")
    n = 2
    yield n

a = my_gen() # Al igual que a los iteradores, debo instanciarlos en un objeto
print(next(a)) #Hello world
print(next(a)) #Hello heaven
print(next(a)) #Hello hell
print(next(a)) #StopIteration error
