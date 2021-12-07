def count_letters(clean_null=False):
    word = str(input("Ingresa la palabra: "))
    response = dict(zip(map(chr, range(0, 256)), [0]*255))
    for countWord in word:
        response[countWord] += 1
    if clean_null:
        response = dict([(k, i) for k, i in response.items() if i > 0])
    print(response)

if __name__ == '__main__':
    count_letters(True)
