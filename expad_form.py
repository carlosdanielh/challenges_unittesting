def expanded_form(numbers):

    len_cero = len(str(numbers)) - 1
    string = ''

    if len_cero != 0:
        for number in str(numbers):
            if int(number) != 0 and len_cero != 0:
                string += f'{number}{str(0) * len_cero} + '
            elif len_cero == 0 and int(number) != 0:
                string += f'{number}'
            len_cero -= 1

        if string[-2] == '+':
            return string[:-3]
        return string
    else:
        return str(numbers)


print(expanded_form(12))  # Should return '10 + 2'
print(expanded_form(42))  # Should return '40 + 2'
print(expanded_form(70304))  # Should return '70000 + 300 + 4'
print(expanded_form(215830))
print(expanded_form(2))

# test.assert_equals(expanded_form(12), '10 + 2');
# test.assert_equals(expanded_form(42), '40 + 2');
# test.assert_equals(expanded_form(70304), '70000 + 300 + 4');


test.describe("Edge Cases")
test.it("Zeros")
test.assert_equals(expanded_form(420370022),
                   '400000000 + 20000000 + 300000 + 70000 + 20 + 2');
test.assert_equals(expanded_form(70304), '70000 + 300 + 4');
test.assert_equals(expanded_form(9000000), '9000000');
test.it("Big Numbers")
test.assert_equals(expanded_form(92093403034573), 
'90000000000000 + 2000000000000 + 90000000000 + 3000000000 +' 
'400000000 + 3000000 + 30000 + 4000 + 500 + 70 + 3');
test.assert_equals(expanded_form(2096039485293),
 '2000000000000 + 90000000000 + 6000000000 + 30000000 + 9000000 + 400000 + 80000 + 5000 + 200 + 90 + 3');