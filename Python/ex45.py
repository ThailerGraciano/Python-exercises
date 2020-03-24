import random as rd
c1=1 
c2=2
c3=3
i=0
lista=[c1, c2, c3]
print(100*'=')
print('Te desafio a ganhar de mim no Jokempô!')
print(100*'=')
while i==0:
    pc=rd.choice(lista)
    print('Suas opções são:\n1-Pedra\n2-Papel\n3-Tesoura')
    print(100*'=')
    escolha=int(input('Digite o número da opção desejada\nFaça sua escolha: '))
    print(100*'=')
    if escolha == pc:
        print('Empate!!')
        if escolha == 1:
            print('Eu também escolhi Pedra')
        elif escolha == 2:
            print('Eu também escolhi Papel ')
        elif escolha == 3:
            print('Eu também escolhi Tesoura ')
    elif escolha == 1 and pc == 2:
        print('Eu ganhei!!\nEscolhi papel')
    elif escolha == 1 and pc == 3:
        print('Você ganhou!!\nEscolhi tesoura')
    elif escolha == 2 and pc == 1:
        print('Você ganhou!!\nEscolhi pedra')
    elif escolha == 2 and pc == 3:
        print('Eu ganhei!!\nEscolhi tesoura')
    elif escolha == 3 and pc == 1:
        print('Eu ganhei!!\nEu escolhi pedra')
    elif escolha == 3 and pc == 2:
        print('Você ganhou!!\nEu escolhi papel')
    else:
        print('Valor incorreto\nTente novamente')
    print(100*'=')
    x=int(input('Você deseja continuar?\n1-Sim\n2-Não\n'))
    if x == 1:
        i==0
    else:
        i=1  
    print(100*'=')      
print('obrigado por jogar!!☺')