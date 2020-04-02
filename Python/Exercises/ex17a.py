co=float(input('Insira o valor do cateto oposto: '))
ca=float(input('Insira o valor do cateto adjascente: '))
hi=(ca**2 + co**2) ** (1/2)
print('o comprimento da hipotenusa é {:.2f}cm'.format(hi))