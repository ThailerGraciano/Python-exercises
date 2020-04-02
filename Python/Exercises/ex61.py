razao=int(input('Digite a razão da PA: '))
pa=int(input('Digite o primeiro termo: '))
print(pa)
progressao=pa + razao
print(progressao)
cont = 0
while cont != 9:
    progressao=progressao + razao
    print(progressao)
    cont += 1