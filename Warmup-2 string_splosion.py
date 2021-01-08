'''
string_splosion('Code') → 'C Co Cod Code'	''	X
string_splosion('abc') → 'a ab abc'	'aababc'	OK
string_splosion('ab') → 'aab'	'aab'	OK
string_splosion('x') → 'x'	''	X
string_splosion('fade') → 'f fa fad fade'	''	X
string_splosion('There') → 'T Th The Ther There'	''	X
string_splosion('Kitten') → 'K Ki Kit Kitt Kitte Kitten'	''	x
string_splosion('Bye') → 'BByBye'	'BByBye'	Ok
string_splosion('Good') → 'G Go Goo Good'	''	x
string_splosion('Bad') → 'B Ba Bad'	'BBaBad'

best alternative:

def string_splosion(str):
  result = ""
  # On each iteration, add the substring of the chars 0..i
  for i in range(len(str)):
    result = result + str[:i+1]
  return result
'''
word = input('ingrese letra')
tamano = len(word)
lista = []
for i in range(tamano):
    lista.append(word[:tamano - i])
lista.reverse()
word = ''.join(lista)
print(word)
