

file = open('text_file.txt', 'w')
file.write("cokolada, mleko, jablko, banan")


def 7_letters_word():
    with open('text_file.txt') as file:
        for line in file:
            for word in line.split():
                if len(word) == 7:
                    print(word)

7_letters_word()


