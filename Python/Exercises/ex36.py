valor=int(input('Digite o valor da casa: '))
sal=int(input('Digite o valor do seu salário: '))
anos=int(input('Digite em quantos anos você pretende pagar: '))

mes=anos * 12
mensalidade=valor / mes
permitido=(sal * 30) / 100

if mensalidade <= permitido:
    print('Seu empréstimo foi aceito com uma parcela de R${:.2f} mensais'.format(mensalidade))
else:
    print('Seu empréstimo foi negado')