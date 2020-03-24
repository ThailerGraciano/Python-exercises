import math
an=float(input('Qaul o ângulo desejado: '))
seno=math.sin(math.radians(an))
cos=math.cos(math.radians(an))
tan=math.tan(math.radians(an))

print('Segue os valores do ângulo {:.2f}'.format(an))
print('O seu seno é {:.2f}'.format(seno))
print('O seu cosseno é {:.2f}'.format(cos))
print('O sua tangente é {:.2f}'.format(tan))