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



