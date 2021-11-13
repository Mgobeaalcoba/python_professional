""" Un decorador es un closure

Un decorador es una función que recibe como parametro otra función,
le añade cosas, la ejecuta y retorna una función diferente (O mejor dicho
a la misma función pero ya modificada).

Veamos ejemplos de decoradores: """

def decorador(func):
    def envoltura():
        func()
        print("Esto se añade a mi función original")
    return envoltura

def saludo():
    print("¡Hola!")

saludo() # Imprimo mi función de forma original

# saludo = decorador(saludo) # Este decorado se puede hacer también
# con "azucar sintactica" o "sugar sintax" usando el "@"

@decorador
def saludo():
    print("¡Hola!")

saludo()
