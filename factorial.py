# -*- coding: utf-8 -*-
def factorial(number):
    if number == 0: 
        return 1
    return number * factorial(number -1)
if __name__ == "__main__":
    number = int(input('¡Escribre un número: '))
    result = factorial(number)
    print(result)