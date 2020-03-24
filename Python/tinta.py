l=float(input('Qual a largura da sua parede?: '))
a=float(input('Qual a altura da sua parede?: '))

m2=a * l
t=9
qt=m2 / t
print(100*'-')
print('Sua parede tem {}m²'.format(m2))
print(100*'-')
dm=int(input('Quantas demaõs você quer passar?: '))
print(100*'-')
qtt=dm * qt

print('\033[0;33;44mVocê precisará de {:.1f} litros de tinta para essa pintura, \npois irá utilizar {:.1f} litros de tinta para cada demão.\033[m'.format(qtt, qt))
print(100*'-')

if qtt>=50:
    print('Ai vai bastante tinta, você pode comprar uma de 50 litros e o resto completar com os outros valores.')
else:
    if qtt>=20:
        print('Recomendamos a compra de uma lata de 50 litros.')
    else:
        if qtt>=10:
            print('Recomendamos a compra de uma lata de tinta de 20 litros.')
        else:
            if qtt>=5:
                print('Recomendamos a compra de uma lata de tinta de 10 litros.')
            else:
                if qtt>=1.5:
                    print('Recomendamos a compra de uma lata de 5 litros.')
                else:
                    print('Recomendamos a compra de uma lata de 1.5 litros.')
x=int(input(100*'-'))