file = open('../test.txt', 'w')
file.write("test text")
file.close()

#pri cteni musi soubor existovat
file = open('../test.txt', 'r')
data = file.read()
file.close()
print(data)

file = open('../test.txt', 'a')
file.write("/n druhy radek")
file.close()
print(data)


