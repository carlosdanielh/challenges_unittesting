import pdb; 
def round_sum(a, b, c):
    
    return round10(a) + round10(b) + round10(c)


def round10(num):
    num_string = str(num)
    tamano_num = len(num_string)
    ultimo_digito = int(num_string[-1])
    primer_digito = int(num_string[0])
    primeros_numeros = abs(2 - tamano_num)
    
    nu = 0
    if tamano_num == 1 and ultimo_digito < 5:
        return 0
    elif tamano_num == 1 and ultimo_digito >= 5 and ultimo_digito <= 10:
        return 10
    elif tamano_num == 2 and ultimo_digito < 5:
        return primer_digito * 10
    elif tamano_num == 2 and ultimo_digito > 5:
        return (primer_digito * 10)+10
    elif tamano_num > 2 and ultimo_digito <= 5:
        nu = int(num_string[:primeros_numeros])*(100)
        suma = nu+(int(num_string[-2])*10)
        return suma
    else:
        nu = int(num_string[:primeros_numeros])*(100)
        suma = nu+(int(num_string[-2])*10)+10
        #pdb.set_trace()
        return suma


print(round_sum(6, 4, 4))
