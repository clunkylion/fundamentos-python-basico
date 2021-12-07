def main():
    #for counter in range(1000):
    #    if counter % 2 != 0:
    #        continue
    #    print(counter)
    #for i in range(1001):
    #    print(i)
    #    if i == 568:
    #        break 
    text = input("Write a Text : ")
    for letter in text:
        if letter == 'o':
            break
        print(letter)

if __name__ == "__main__":
    main()