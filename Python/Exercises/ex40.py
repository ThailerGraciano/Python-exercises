print(100 * '¬¬')
n1=float(input('Insira sua primeira nota: '))
print(100 * '¬¬')
n2=float(input('Insira a sua segunda nota: '))
media=(n1 + n2) / 2
print(100 * '¬¬')
if media >= 7:
    print('Parabéns você foi aprovado com a média de {:.2f}'.format(media))
elif media >= 5:
    print('Bom, sua média é {:.2f} você precisará realizar a recuperação'.format(media))
else:
    print('Sua média de {:.2f} não é o suficiente para ser aprovado, você foi REPROVADO!')
print(100 * '¬¬')