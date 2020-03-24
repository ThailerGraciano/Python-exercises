km=float(input('Quantos Km você rodou com o carro: '))
dias=float(input('Quantos dias você ficou com o carro: '))
vkm=km * 0.15
vda=dias * 60
vf=vda + vkm

print('O valor final do aluguel é de R${}, R${} pela Kilometragem e R${} pelos dias alugado'.format(vf, vkm, vda))