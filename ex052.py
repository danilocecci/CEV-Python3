import colorama
colorama.init()

print('-='*9+'-')
print('\033[1;31m  NÚMEROS PRIMOS\033[m')
print('-='*9+'-')

print('Vamos descobrir se um número é primo ou não :D')

number = int(input('Digite um número: '))
result = [1]
end = int(number/2+1)


for c in range(1,end):
    if number%c == 0:
        result.append(c)

result.append(number)
result.remove(1)
if len(result)>2:
    print('{} não é um número primo! Pois é divisível por {}'.format(number,result))
else:
    print('{} é um número primo! Pois é divisível apenas por {}'.format(number, result))
