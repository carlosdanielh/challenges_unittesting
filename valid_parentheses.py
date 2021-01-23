'''
Write a function called that takes a string of parentheses, and determines if 
the order of the parentheses is valid. The function should return true if the 
string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid
 ASCII characters. Furthermore, the input string may be empty and/or not 
 contain any parentheses at all. Do not treat other forms of brackets as 
 parentheses (e.g. [], {}, <>).
 '''


def pair(string):
    lista = [element for element in list(string) if element == '(' or
             element == ')']
    string = ''.join(lista)

    if len(string) % 2 == 0:
        counter = len(string) // 2

        while True:
            string = string.replace('()', '')

            if counter == 0:
                if string == '':
                    return True
                else:
                    return False

            counter -= 1
    else:
        return False


print(pair('(()(s))((2()(d))(g)))')
print(pair("()"))
print(pair(')(()))'))
print(pair("("))
print(pair("(())((()())())"))
print(pair("hi())("))
