'''
write a fuction, persistence that takes in a positive parameter num and returns
its multiplicative persistence, which is the number of times you must multiply
the digits in num until you reach a single digit,.

persistence(39) 3*9 27 2*7 14 1*4 4
persistence(999) 9*9*9 729 7*2*9 126 1*2*6 12 1*2 2
persistence(4) return 0 because its just one digit.
'''


def persistence(number):
    if len(str(number)) == 1:
        return 0

    lista = list(str(number))
    mult = 1
    while mult == 1:
        for number in lista:
            mult *= number

        if len(str(mult)) == 1:
            return mult
        else:
            lista = list(str(mult))
            mult = 1
            lista = [int(num) for num in lista]


print(persistence(39))
print(persistence(999))
print(persistence(4))
print(persistence(18))