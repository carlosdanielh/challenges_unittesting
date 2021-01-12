from math import sqrt


def comp(a, b):
    t = len(a)

    if len(a) == len(b) and None not in [a, b]:
        list_square = [sqrt(element) for element in b]
        for element in list_square:
            if element not in a:
                return False
        return True
    else:
        return False

try:
    pass
except expression as identifier:
    pass
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

print(comp(a, b))