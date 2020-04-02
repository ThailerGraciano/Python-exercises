slr=int(input('Informe o valor do seu salário: '))

if slr>1250:
    aumento=slr*0.1
    slrtt=aumento+slr
    print('Seu salário será de R${} com o aumento de R${}'.format(slrtt, aumento))
else:
    aumento=slr*0.15
    slrtt=aumento+slr
    print('Seu salário será de R${} com o aumento de R${}'.format(slrtt, aumento))