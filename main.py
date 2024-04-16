"""

file = open('test.txt', 'w')
file.write("test text")
file.close()

#pri cteni musi soubor existovat
file = open('test.txt', 'r')
data = file.read()
file.close()
print(data)

file = open('test.txt', 'a')
file.write("/n druhy radek")
file.close()
print(data)

"""
import fileinput

"""
def word7(source_file, dest_file, threshold):
    print("read data from file")
    file_handler = open(source_file, 'r')
    date = file_handler.read()
    file_handler.close()

    print("split data")
    output_data = []
    split_data = date.split(" ")
    print(type(split_data)) # overi druh typu

    print("filter data")
    for word in split_data:
        if len(word) >= threshold:
            output_data.append(word)

    print("write data to file")
    file_handler = open(dest_file, 'w')
    file_handler.writelines(output_data)
    file_handler.close()
    print("finished")


word7('text_file.txt', '7_letters_words.txt', 7)

print("kontrolni vysledek")
print(open('7_letters_words.txt', 'r').read())

"""
"""
# otoci cele slovo pozpatku !!!

def reverse(source_file, dest_file):
    print("read data from file")
    file_handler = open(source_file, 'r')
    date = file_handler.read()
    file_handler.close()

    print("reverse data")
    output_data = date[::-1]

    print("write data to file")
    file_handler = open(dest_file, 'w')
    file_handler.write(output_data)
    file_handler.close()
    print("finished")

reverse('text_file.txt', 'reversed_text_file.txt')
print(open('reversed_text_file.txt', 'r').read())

"""

def reverse(source_file, dest_file):
    print("read data from file")
    fi
"""le_handler = open(source_file, 'r')
    data = file_handler.readlines()
    file_handler.close()

    file_handler = open(dest_file, 'w')
    file_handler.close()

    file_handler = open(dest_file, 'a')
    for i in range(len(data) - 1, -1, -1):
        file_handler.write(data[i])
        file_handler.close()

    print("finished")


reverse('Lekce11/text_file.txt', 'Lekce11/reversed_text_file2.txt')
print(open('Lekce11/reversed_text_file2.txt', 'r').read())





