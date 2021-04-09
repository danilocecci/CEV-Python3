data = [[],[]]
num = 0

for c in range(0,7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        data[0].append(num)
    else:
        data[1].append(num)

data[0].sort()
data[1].sort()
print(f'Números pares cadastrados: {data[0]}')
print(f'Números ímpares cadastrados: {data[1]}')