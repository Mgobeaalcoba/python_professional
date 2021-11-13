""" Este closure retorno una función que returna 
la división de un numero x por un numero n"""

def make_division_by(n):
    def division(x):
        return x / n
    return division

division_by_3 = make_division_by(3)
division_by_5 = make_division_by(5)
division_by_18 = make_division_by(18)

print(division_by_3(18))
print(division_by_5(100))
print(division_by_18(54))
