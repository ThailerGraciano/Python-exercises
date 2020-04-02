print(100 * '-')
ano=int(input('em que ano você nasceu?: '))
print(100 * '-')
idade=2020 - ano
if idade > 18:
    dif=idade - 18
    confirm=str(input('Você já se alistou ?\n\nDigite S pra sim ou N para não: '))
    if confirm == 's' or confirm == 'S':
        print(100 * '-')
        print('Que ótimo, então está tudo certo!!')
    elif confirm == 'n' or confirm == 'N':
        print(100 * '-')
        print('Você deveria ter se alistado há {} anos'. format(dif))
    else:
        print(100 * '-')
        print('\033[1;31;43mResposta inválida.\033[m')
elif idade >= 17:
    confirm=str(input('Você já se alistou ?\n\nDigite S pra sim e N para não: '))
    if confirm == 's' or confirm == 'S':
        print(100 * '-')
        print('Que ótimo, então está tudo certo, só resta esperar \nas datas de comparecimento a junta militar!!')
    elif confirm == 'n' or confirm == 'N':
        print(100 * '-')
        print('Já é bom você ficar atento as datas e prazos para o alistamento!')
    else:
        print(100 * '-')
        print('\033[1;31;43mResposta inválida.\033[m')
else:
    dif=18 - idade
    print('Você ainda é novo para se alistar no exército\nfaltam {} anos para você se alistar'.format(dif))            

print(100 * '-')