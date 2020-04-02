print(100*'¬')
print('Olá seja bem vindo ao medidor de IMC')
print(100*'¬')
peso=float(input('Digite agora o seu peso em KG: '))
print(100*'¬')
altura=float(input('Digite agora sua altura em metros: '))
imc=peso / altura ** 2
print(100*'¬')
if imc > 40:
    print('Seu IMC é {:.2f}\nCuidado! você tem obesidade morbida, procure um especialista!'.format(imc))
elif imc > 30:
    print('Seu IMC é {:.2f}\nCuidado! você está obesidade, procure um especialista'.format(imc))
elif imc > 25:
    print('Seu IMC é {:.2f}\nCuidado! você está com sobrepeso, procure um especialista'.format(imc))
elif imc > 18.5:
    print('Seu IMC é {:.2f}\nTudo certo! você está em seu peso ideal, continue se cuidando para se manter assim'.format(imc))
else:
    print('Seu IMC é {:.2f}\nCuidado! Você está abaixo do peso, procure um especialista'.format(imc))
print(100*'¬')