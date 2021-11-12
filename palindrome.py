def is_palindrome(string: str) -> bool: # Le indico con -> que la función debe devolver un valor booleano
    string = string.replace(" ","").lower() #Elimino los espacios vacios con el metodo replace y dejo todo en minuscula con el metodo lower
    return string == string[::-1] #Uso slices para dar vuelta la palabra y ver si es palindromo o no.

def run():
    print(is_palindrome(True))

if __name__ == '__main__':
    run()