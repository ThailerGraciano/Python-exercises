print(100 * '¬¬')
ano=int(input('Qual o ano de nascimento do aluno?: '))
idade=2020 - ano
print(100 * '¬¬')
if idade > 20:
    print('O aluno tem {} anos, ele já está na categoria MASTER'.format(idade))
elif idade == 20:
    print('O aluno tem {} anos, ele já está na categoria SÊNIOR'.format(idade))
elif idade > 14:
    print('O aluno tem {} anos, ele já está na categoria JUNIOR'.format(idade))
elif idade > 9:
    print('O aluno tem {} anos, ele já está na categoria INFANTIL'.format(idade))
else:
    print('O aluno tem {} anos, ele já está na categoria MIRIM'.format(idade))
print(100 * '¬¬')