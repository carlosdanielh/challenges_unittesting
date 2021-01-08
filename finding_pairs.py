import random

###############################################################################
# number_sum = int(input('enter a number sum: \n'))

# number_pair = number_sum / 2
# found = False
# lista_no_found = []
# while not found:
#     list_n = [random.randint(1, 9) for number in range(4)]
#     index_found = ''
#     cont = 0

#     for index, element in enumerate(list_n):
#         if element == number_pair:
#             cont += 1
#             index_found += str(index)

#     if cont == 2:
#         found = True

#     if not found:
#         lista_no_found.append(list_n)

# for number, listas in enumerate(lista_no_found):
#     print(f'no se encontro pair en esta lista --> #{number + 1} {listas}')

# number_found = len(lista_no_found) + 1 
# print(f'but was found in this ---> #{number_found} {list_n}')
# print(f'{number_pair} + {number_pair} = {number_sum} '
#       f'with index {index_found[0]} and {index_found[1]}')

###############################################################################
number_sum = int(input('enter a number sum: \n'))
index_found = ''
lista_no_found = []
found = False
while not found:
    list_n = [random.randint(1, 9) for number in range(4)]

    for index, element in enumerate(list_n):
        # pair_to_find = abs(element - number_sum)

        for index2, element2 in enumerate(list_n):

            if index != index2 and sum([element, element2]) == number_sum:
                index_found = f'{index}{index2}'
                elements = f'{element}{element2}'
                found = True
                break
    if found:
        break
    else:
        lista_no_found.append(list_n)

for number, listas in enumerate(lista_no_found):
    print(f'no se encontro pair en esta lista --> #{number + 1} {listas}')

number_found = len(lista_no_found) + 1
print(f'but was found in this ---> #{number_found} {list_n}')
print(f'{elements[0]} + {elements[1]} = {number_sum}'
      f'with index {index_found[1]} and {index_found[0]}')
