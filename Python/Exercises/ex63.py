print(10 * '-=')
seq = int(input('Quantos termos você deseja descobrir da sequência de Fibonacci: '))
cont = 0
anterior = 0
atual = 0
print(10 * '-=')
print(atual, end=" -> ")
while cont != seq - 2:
    if atual == 0:
        atual = 1
        print(atual, end=" -> ")
    atual = anterior + atual
    anterior = atual - anterior
    print(atual, end=" -> ")   
    cont += 1
print('FIM !\n', 10 * '-=')