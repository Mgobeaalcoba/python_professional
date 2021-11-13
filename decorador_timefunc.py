from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs): # Ver mensaje debajo
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron "+str(time_elapsed.total_seconds())+" segundos.")
    return wrapper

@execution_time # Decoro la función que tengo debajo con el decorador que construí arriba
def random_func():
    for x in range(1,1000000):
        pass

@execution_time
def sum(a: int, b: int) -> int:
    return a + b

@execution_time
def saludo(nombre="Cesar"): # Fijo un parametro por defecto. Un Kwargs
    print("Hola "+ nombre)

""" 
Si decoro la funcion sum, dejando la función wrapper sin argumentos
no se va a ejecutar y va a correr un TypeError ya que sum tiene 2 
argumentos y wrapper no tiene ninguno. Para lograr que wrapper funcione
con cualquier cantidad de argumentos nombrados y sin nombrar debo 
agregar como paramentros de la función (*args, **kwargs)
"""

sum(5, 5)
random_func() #Ejecuto mi random_func decorada.
saludo("Mariano")
saludo()
