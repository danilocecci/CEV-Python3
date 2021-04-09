matrix = list()
values = list()
eve_sum = third_column_sum = max_second_line = 0

for c in range(0,3):
    for x in range(0,3):
        values.append(int(input(f'Digite um número para a posição [{c},{x}]: ')))
    matrix.append(values[:])
    values.clear()
print('-='*10+'-')

for c in range(0,3):
    for x in range(0,3):
        print(f'[{matrix[c][x]:^5}]', end='')
        if matrix[c][x] % 2 == 0:
            eve_sum += matrix[c][x]
        if x == 2:
            third_column_sum += matrix[c][x]
        if c == 1 and matrix[c][x] > max_second_line:
            max_second_line = matrix[c][x]
    print('')
print('-='*10+'-')
print(f'A soma dos valores pares é {eve_sum}!')
print(f'A soma dos valores da terceira coluna é {third_column_sum}!')
print(f'O maior valor da segunda linha é {max_second_line}!')