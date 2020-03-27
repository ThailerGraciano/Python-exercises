p1=int(input('Insira peso de 5 pessoas\n1°: '))
p2=int(input('2°: '))
p3=int(input('3°: '))
p4=int(input('4°: '))
p5=int(input('5°: '))

lista=[p1, p2, p3, p4, p5]

print('O maior peso foi o de {}Kg'.format(max(lista)))
print('O menor peso é o de {}Kg'.format(min(lista)))