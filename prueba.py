values = 'aaarbbcaaaaaabb'
dictionary = {}
for value in values:
    if value in dictionary:
        dictionary[value] +=1
    else:
        dictionary[value] = 1
for v, value in dictionary.items():
    print({v, value})