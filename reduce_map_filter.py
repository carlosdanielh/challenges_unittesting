###############################################################################
#  it will return all even number, just because lambda return true to the expre
#  we assigned with filter.
lista = [number for number in range(0, 11)]

print(lista)

print(list(filter(lambda x: x % 2 == 0, lista)))
###############################################################################
# for each elemente of the list will be apply what the function return to each
# element.
print(list(map(lambda x: str(x), lista)))