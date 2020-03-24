razao=int(input('Digite a razão da PA: '))
pa=int(input('Digite o primeiro termo: '))
print(pa)
progressao=pa + razao
print(progressao)
for cont in range (0, 8):
    progressao=progressao + razao
    print(progressao)
