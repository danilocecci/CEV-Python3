keep = 's'
num = list()

while keep == 's':
    num_handle = int(input('Digite um número: '))
    num.append(num_handle)
    keep = input('Deseja continuar? [S/N]').lower()
print(f'Fora inseridos {len(num)} números!')
num.sort(reverse=True)
print(f'Os números em ordem descrente foram: {num}')
if 5 in num:
    print('O número 5 está na lista!')
else:
    print('O número 5 não está na lista!')