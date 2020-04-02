num=int(input('Digite um valor para saber sua tabuada: '))
multi=1
result=num * multi
  
print('-' * 12)
while (multi <= 10):
    print('{} x {:2} = {:3}'.format(num, multi, result))
    multi=multi + 1
    result=num * multi
    if(multi > 10):
        print('-' * 12)
        print('FIM!')     