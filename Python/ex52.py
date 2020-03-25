num=int(input('Insira o número que você deseja descobrir se é primo: '))

primos=[]

for x in range(1, 101):
    cont=0

    for y in range(1, x+1):
        if x%y==0:
            cont+=1
    if cont<=2:
        primos.append(x)

if num in primos:
    print('{} é um número primo'.format(num))
else:
    print('{} não é um número primo'.format(num))
    
ind=int(input('Se você deseja visualizar uma lista com números primos digite "1": '))

if ind == 1:
    print(primos)
    print('OK, até mais!!')
else:
    print('OK, até mais!!')