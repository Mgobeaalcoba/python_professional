def is_prime(number: int) -> bool:
    prime = True
    for i in range(2,number):
        if number % i == 0:
            prime = False
            break
    return prime

def run():
    print(is_prime(11))

if __name__ == '__main__':
    run()
