import random
num=random.randint(0,5)
user=int(input('Digite um número de 0 a 5 e tente acertar em qual estou pensando: '))
tent=1
if user == num:
    print('Parabéns você acertou na primeira tentativa, eu também estava pensando no número {}'.format(num))
else:
    while user != num:
        print('tente novamente!')
        user=int(input('Digite um número de 0 a 5 e tente acertar em qual estou pensando: '))
        tent += 1
    print('Parabéns você acertou na {}° tentativa\nEu sempre estive pensando no número {}'.format(tent, num))