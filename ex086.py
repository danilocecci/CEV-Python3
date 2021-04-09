matrix = list()
values = list()

for c in range(0,3):
    for x in range(0,3):
        values.append(int(input(f'Digite um número para a posição [{c},{x}]: ')))
    matrix.append(values[:])
    values.clear()

for c in range(0,3):
    for x in range(0,3):
        print(f'[{matrix[c][x]:^5}]', end='')
    print('')