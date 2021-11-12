#Ejemplo usado en pruebas técnicas:

def make_multiplier(x):

    def multiplier(n):
        print(n) # Para seguir que valor asume
        print(x) # Para seguir que valor asume
        return x * n

    return multiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(3))
print(times4(5))
print(times10(times4(2)))
