cont = 0
val = 0
n = 0
while val != 999:
    val = int(input('Digite um valor: '))
    cont += 1
    n = n + val
print('FIM! você digitou {} números'.format(cont))
print('A soma deles é {}'.format(n))