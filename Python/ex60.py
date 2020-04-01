from math import factorial
print(100 * '¬')
n = int(input('Digite um valor para descobrir seu fatorial: '))
c = n
f = factorial(n)
print(100 * '¬')
while c > 1:
    print('{} x '.format(c), end='')
    c -= 1
if c == 1:
    print('{} = {}'.format(c, f))
print(100 * '¬')