print('Por favor, insira o ano de nascimento de 7 pessoas:')
p1=int(input('1°:'))
p2=int(input('2°:'))
p3=int(input('3°:'))
p4=int(input('4°:'))
p5=int(input('5°:'))
p6=int(input('6°:'))
p7=int(input('7°:'))

p1=2020 - p1
p2=2020 - p2
p3=2020 - p3
p4=2020 - p4
p5=2020 - p5
p6=2020 - p6
p7=2020 - p7

lista=[p1, p2, p3, p4, p5, p6, p7]
lista_maior=[]
lista_menor=[]

for elem in lista:
    if elem >= 21:
        lista_maior.append(elem)

    elif elem < 21:
        lista_menor.append(elem)


print('Há {} maiores de 21 anos'.format(len(lista_maior)))
print('Há {} menores de 21 anos'.format(len(lista_menor)))