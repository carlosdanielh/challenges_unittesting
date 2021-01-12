def dig_pow(number, p):
    list_number = list(str(number))
    list_number = list(map(int, list_number))
    start_pow = p
    list_power = []

    for n in list_number:
        list_power.append(pow(n, start_pow))
        start_pow += 1
    suma = sum(list_power)
    result = suma % number
    if result == 0:
        return int(suma/number)
    else:
        return -1


def dig_pow2(n, p):
    s = 0
    for i, c in enumerate(str(n)):
        s += pow(int(c), p + i)
    return s / n if s % n == 0 else -1


print(dig_pow2(89, 1))
print(dig_pow2(92, 1))
print(dig_pow2(695, 2))
print(dig_pow(3456789, 1))
print(dig_pow(46288, 5))
print(dig_pow(3456789, 5))

# dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
# dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
# dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
# dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51