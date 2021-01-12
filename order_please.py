def order(cadena):

    if cadena != '':
        sort_list = []
        for element in cadena.split():
            for number in range(1, len(cadena.split())+1):
                if str(number) in element:
                    sort_list.append(element)
                    break
        return ' '.join(sort_list)
    else:
        return ''


print(order("is2 Thi1s T4est 3a"))