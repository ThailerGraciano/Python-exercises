num=int(input('Digite um número para conversão: '))
print(100 * '-')
print('Agora escolha algumas das bases para conversão')
print(100 * '-')
print('[ 1 ] para BINÁRIO')
print('[ 2 ] para OCTAL')
print('[ 3 ] para HEXADECIMAL')
print(100 * '-')
opcao=int(input('Digite sua opção: '))
print(100 * '-')
if opcao == 1:
    print('{} convertido para binário é {}'.format(num, bin(num)))
elif opcao == 2:
    print('{} convertido para octal é {}'.format(num, oct(num)))
elif opcao == 3:
    print('{} convertido para hexadecimal é {}'.format(num, hex(num)))
else:
    print('Opção inválida.')