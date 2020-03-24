print(100 * '¬')
valor=int(input('-> Valor do produto: '))
print(100 * '¬')
print('-> Qual será a opção de pagamento?\n\n1 - À vista (dinheiro ou cheque)\n2 - Débito\n3 - Até duas vezes no cartão\n4 - três vezes ou mais')
escolha=int(input('-> '))
print(100 * '¬')
if escolha == 1:
    pf=valor - (valor * 0.10) 
    print('O valor com 10% de desconto é R${}'.format(pf))
elif escolha == 2:
    pf=valor - (valor * 0.05) 
    print('O valor com 5% de desconto é R${}'.format(pf))
elif escolha == 3:
    parcela=valor / 2
    print('O valor sem juros é 2x de R${}'.format(parcela))
elif escolha == 4:
    vezes=int(input('Em quantas vezes será o pagamento?\n-> '))
    print(100 * '¬')
    pf=valor + (valor * 0.20)
    parcela=pf / vezes
    print('O valor total da compra é de R${},\nparcelado em {}x de R${}'.format(pf, vezes, parcela))
else:
    print('Por favor insira um valor válido, Tente novamente!')
print(100 * '¬')
print('_|_|_\n_|_|_\n | | ')