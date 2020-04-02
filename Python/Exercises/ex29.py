vel=int(input('Digite o valor da sua velocidade: '))
 
if vel>80:
     dif=vel-80
     val=dif*7
     print('Sua velocidade está {}Km acima do permitido, sua multa será de R${}.'.format(dif, val))
else:
        print('Sua velocidade está dentro do limite.')
    