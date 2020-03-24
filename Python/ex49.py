num=int(input('Digite um valor para saber sua tabuada: '))
print(50 * '-=')
for cont in range(0, 11):
    result=num * cont
    print('{} x {} = {}'.format(num, cont, result))
print(50 * '-=')