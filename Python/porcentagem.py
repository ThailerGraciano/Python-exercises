val1=float(input('Insira o primeiro valor: '))
val2=float(input('Insira agora quantos por cento esse numero equivale: '))
val3=float(input('Insira qual a porcentagem que você pretende descobrir: '))
porc=(val1 * val3) / val2
div4=porc / 4
div8=porc / 8
print('{} será o valor pago ja com desconto'.format(porc))
print('Pode ser dividido em 4 de R${:.0f} \nou em 8 de R${}'.format(div4, div8))