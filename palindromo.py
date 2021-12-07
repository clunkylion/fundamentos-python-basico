def palindrome():
    word = str(input('Escribe una Palabra : '))
    if(word == word[::-1]):
        print('La palabra '+word+' palíndroma')
    else:
        print('La palabra '+word+' NO es palíndroma')

if __name__ == '__main__':
    palindrome()