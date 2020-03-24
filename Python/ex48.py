from time import sleep
soma=0
for cont in range(0, 501):
    sleep(0.01)
    numero=cont % 2
    if numero == 1:
        soma=soma +cont
        print('+ {}'.format(cont))
print('={}'.format(soma))