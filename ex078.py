num = list()
max_ones = list()
min_ones = list()

for count in range(0,5):
    num.append(int(input(f'Digite um número na {count+1}ª posição: ')))
print(f'Os números que você digitou foram: {num}')

for count in range(0,5):
    if num[count] == max(num):
        max_ones.append(count+1)

for count in range(0,5):
    if num[count] == min(num):
        min_ones.append(count+1)

str_min_ones = map(str, min_ones)
str_max_ones = map(str, max_ones)

if len(min_ones) > 1:
    print(f'O menor número informado foi o "{min(num)}" nas posições '+', '.join(str_min_ones)+'.')
else:
    print(f'O menor número informado foi o "{min(num)}" na posição {str_min_ones}.')

if len(max_ones) > 1:
    print(f'O maior número informado foi o "{max(num)}" nas posições '+', '.join(str_max_ones)+'.')
else:
    print(f'O maior número informado foi o "{max(num)}" na posição {str_max_ones}.')