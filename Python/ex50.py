resultado=0
for cont in range (0, 6):
    n1=int(input('Insira um valor: '))
    x=n1 % 2
    if x == 0:
        resultado=resultado + n1
print('A soma de todos números pares digitado é {}'.format(resultado))