sexo = str (input( 'Digite seu sexo [ M | F ]: '))
sexo = sexo.upper()
while  sexo  !=  'M' and sexo != 'F':
    print ( 'Valor incorreto, tente novamente.' )
    sexo = str (input( 'Digite seu sexo [ M | F ]:'))
    sexo = sexo.upper()
if sexo == 'M':
    print('Você optou pelo sexo Masculino!')
elif sexo == 'F':
    print('Você optou pelo sexo Feminino')