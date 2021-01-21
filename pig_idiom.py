'''
Simple Pig Latin
Move the first letter of each word to the end of it, then add "ay" to the end 
of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''


def pig_it(cadena):
    concatenate = ''

    for element in cadena.split():
        if element[-1].isalpha():
            concatenate += element[1:] + element[0] + 'ay' + ' '
        else:
            if len(element) != 1:
                concatenate += element[1:] + element[0] + 'ay' + element[-1] +\
                               ' '
            else:
                concatenate += element

    return concatenate.strip()


#  clever way...
def pig_it2(text):
    lst = text.split()
    return ' '.join([word[1:] + word[:1] + 'ay' if word.isalpha() else word
                    for word in lst])


print(pig_it('Pig latin is cool'))  # igPay atinlay siay oolcay
print(pig_it('Hello world !'))  # elloHay orldway !
