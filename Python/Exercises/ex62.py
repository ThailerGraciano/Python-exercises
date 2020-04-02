razao=int(input('Digite a razão da PA: '))
pa=int(input('Digite o primeiro termo: '))
print(pa, end=' -> ')
progressao=pa + razao
print(progressao, end=' -> ')
cont = 0
mais = 10
var = 8
while mais != 0:
    while cont != var:
        progressao=progressao + razao
        print(progressao, end=' -> ')
        cont += 1
    print('PAUSA')
    mais = int(input(' Quantos termos você quer mostrar a mais: '))
    var = mais
    cont = 0
print('FIM !')