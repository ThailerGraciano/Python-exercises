n1=int(input('Insira o  primeiro valor: '))
n2=int(input('Insira o segundo valor: '))
print(100 * '¬')
print('Agora selecione a operação desejada\n1-Somar\n2-Multiplicar\n3-Maior\n4-Novos Numeros\n5-Sair do programa')
escolha=1
escolha=int(input('=>'))

while escolha != 5:
    if escolha == 1:
        soma=n1 + n2
        print(100 * '¬')
        print('A soma de {} e de {} é igual a {}'.format(n1, n2, soma))
        print(100 * '¬')
        print('Selecione a operação desejada\n1-Somar\n2-Multiplicar\n3-Maior\n4-Novos Numeros\n5-Sair do programa')
        escolha=int(input('=>'))
    elif escolha == 2:
        multi=n1 * n2
        print(100 * '¬')
        print('A multiplicação de {} com {} é igual a {}'.format(n1, n2, multi))
        print(100 * '¬')
        print('Selecione a operação desejada\n1-Somar\n2-Multiplicar\n3-Maior\n4-Novos Numeros\n5-Sair do programa')
        escolha=int(input('=>'))
    elif escolha == 3:
        print(100 * '¬')
        if n1 > n2:
            print('O maior número entre {} e {} é {}'.format(n1, n2, n1))
        elif n1 < n2:
            print('O maior número entre {} e {} é {}'.format(n1, n2, n2))
        
        print('Selecione a operação desejada\n1-Somar\n2-Multiplicar\n3-Maior\n4-Novos Numeros\n5-Sair do programa')
        escolha=int(input('=>'))
    elif escolha == 4:
        print(100 * '¬')
        print('Digite seus novos números:')
        n1=int(input('Primeiro: '))
        n2=int(input('Segundo: '))
        print(100 * '¬')
        print('Selecione a operação desejada\n1-Somar\n2-Multiplicar\n3-Maior\n4-Novos Numeros\n5-Sair do programa')
        escolha=int(input('=>'))

print(100 * '¬')
print('Até mais !')