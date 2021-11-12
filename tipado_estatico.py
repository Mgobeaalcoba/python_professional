# Modulo mypy es el que nos permite trabajar con tipado estático en Python. Se complementa con el modulo typing
# ventajas del tipado estatico: nos da claridad y calidad al codigo y ademas nos va a devolver los errores antes de
# que el programa se ejecute. Como lo hacen Java y como la hacen C. Sirve para identificar errores en capas profundas
# de nuestro codigo!!!

from typing import Dict, List, Tuple
# Las tuplas son inmutables. No puedo modificarlas luego de crearlas

def run():
    positives: List[int] = [1,2,3,4,5]

    users: Dict[str, int] = {
        'argentina': 1,
        'mexico': 34,
        'colombia': 45
    }

    countries: List[Dict[str, str]] = [
        {
            'name': 'Argentina',
            'people': '450000'
        },
        {
            'name': 'Mexico',
            'people': '9000000'
        },
        {
            'name': 'Colombia',
            'people': '999999999999'
        }
    ]

    numbers: Tuple[int, float, int] = (1, 0.5, 1)

    print(type(countries[0]))
    print(type(numbers))

    # En python puedo guardar en una variable, por ej "CoordinatesType" el tipado estatico que luego quiero asignarle a otras variables mediante los ":"
    CoordinatesType = List[Dict[str, Tuple[int, int]]]

    coordinate: CoordinatesType = [
        {
            'coord1': (1,2),
            'coord2': (3,5)
        },
        {
            'coord1': (0,1),
            'coord2': (2,5)
        }
    ]

if __name__ == '__main__':
    run()