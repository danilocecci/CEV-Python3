keep = 's'
num = 0
values = list()
sorted_values = list()

while keep == 's':
    num = int(input('Digite um valor: '))
    if num in values:
        print(f'O valor {num} já existe na lista, portanto não será adicionado novamente.')
        keep = input('Deseja continuar? [S/N] ').lower()
    else:
        values.append(num)
        print('Valor adicionado na lista!')
        keep = input('Deseja continuar? [S/N] ').lower()

values.sort()
print('-='*20+'-')
print(f'Você digitou os valores {values}')