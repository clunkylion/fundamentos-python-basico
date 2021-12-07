def main():
    name = input("Write your name please ... ")
    for letter in name:
        print(letter)
    phrase = input("Write a Phrase: ")
    for character in phrase:
        print(character.upper())
if __name__ == "__main__":
    main()