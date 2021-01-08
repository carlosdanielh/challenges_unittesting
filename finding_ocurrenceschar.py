def find_first_occurrence(word):

    lista_word = list(word)
    for index, letter in enumerate(word):
        for index2, letter_loop in enumerate(lista_word):
            if letter == letter_loop and index != index2:
                return letter


def find_first_occurrence_part2(word):
    lista = []
    for letter in word:
        if letter in lista:
            return letter
        else:
            lista.append(letter)


def find_first_no_occurrence(word):

    lista_word = list(word)
    for index, letter in enumerate(word):
        cont = 0
        for index2, letter_loop in enumerate(lista_word):
            if letter == letter_loop and index != index2:
                cont += 1
            if cont == 1:
                break
        if cont == 0:
            return letter

for number in range(15,-1,-1):
    print(number)

    
print(find_first_occurrence('bjkb'))
print(find_first_occurrence_part2('ajbjabicc'))
print(find_first_no_occurrence('asd1fghjkasdfhjkp'))