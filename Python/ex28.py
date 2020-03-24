import random
num=random.randint(0,5)
user=int(input('Digite um número e tente acertar em qual estou pensando: '))

if user==num:
    print('Parabéns você acertou estou pensando no número {} mesmo'.format(user))
else:
    print('Poxa você errou, na real estou pensnado no número {}'.format(num))