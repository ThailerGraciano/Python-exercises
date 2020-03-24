from math import hypot
co=float(input('Insira o valor do cateto oposto: '))
ca=float(input('Insira o valor do cateto adjascente: '))
hi=hypot(co, ca)
print('A hipotenusa é igual a {}'.format(hi))