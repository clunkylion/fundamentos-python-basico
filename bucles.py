def main():
    LIMIT = 1000000
    counter = 0
    potency_2 = 2**counter
    while potency_2 <= LIMIT:
        print('2 elevado a ' + str(counter)+' es igual a: ' + str(potency_2))
        counter = counter+1
        potency_2 = 2**counter


if __name__ == '__main__':
    main()
