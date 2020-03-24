distancia=int(input('Qual a distância da viagem em Km: '))

if distancia<=200:
    valor=distancia*0.5
    print('Sua viagem sairá em torno de R${}'.format(valor))
else:
    valor=distancia*0.45
    print('Sua viagem sairá em torno de R${}'.format(valor))