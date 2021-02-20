a=[1, 2, 3, 3]

a = list(map(str,a))
if type(a) == str:
        print('entro')
        a=list(a)

for index, element in enumerate(a):
    if index != 0 and element != a[index - 1] and a[index - 1] != '|' :        
        a.insert(index,'|')
print(a)
b = ''.join(a).split('|')

in_order = [''.join(set(element)) for element in b]

print(in_order)