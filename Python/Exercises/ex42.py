print(25*'--')
print('Analisador de Triângulos')
print(25*'--')
r1=int(input('Insira o valor da primeira reta: '))
r2=int(input('Insira o valor da segunda reta: '))
r3=int(input('Insira o valor da terceira reta: '))
print(25*'--')
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas PODEM FORMAR um triângulo')
else:
    print('Essas retas NÃO PODEM formar um triângulo')