l=int(input('Digite a largura da parede em metro(s): '))
a=int(input('Digite a altura da parede em metro(s): '))
m=l * a
t=2
p=m / t

print('Sua parede tem um total de {} m², você precisa de {} litro(s) de tinta para pinta-lá'.format(m, p))