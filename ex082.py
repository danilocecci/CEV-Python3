keep = 's'
num = list()
odd_num = list()
eve_num = list()

#First Option
# while keep == 's':
#     num_handle = int(input('Digite um número: '))
#     keep = input('Deseja continuar? [S/N] ').lower()
#     num.append(num_handle)
#     if num_handle % 2 == 0:
#         eve_num.append(num_handle)
#     else:
#         odd_num.append(num_handle)

#Second Option
while keep == 's':
    num_handle = int(input('Digite um número: '))
    keep = input('Deseja continuar? [S/N] ').lower()
    num.append(num_handle)
for c in range(0,len(num)):
    if num[c] % 2 == 0:
        eve_num.append(num[c])
    else:
        odd_num.append(num[c])

print(f'Lista completa: {num}')
print(f'Lista com números pares: {eve_num}')
print(f'Lista com números ímpares: {odd_num}')