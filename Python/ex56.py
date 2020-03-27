print('CADASTRO')
lista_nome=[]
lista_idade=[]
lista_sexo=[]
for cont in range (1, 5):
    print(50 * '¬')
    print('{}° pessoa'.format(cont))
    name=str(input('Nome: '))
    lista_nome.append(name)
    age=int(input('Idade: '))
    lista_idade.append(age)
    sex=(str(input('Sexo: ')))
    lista_sexo.append(sex)
print(50 * '¬')
print(lista_nome)
print(lista_idade)
print(lista_sexo)
med=sum(lista_idade) / cont
print(med)