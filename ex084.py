keep = 's'
people = list()
data = list()
heaviest = 0
lighter = 0
heaviest_ones = list()
lighter_ones = list()

while keep == 's':
    data.append(str(input('Nome: ')))
    data.append(float(input('Peso(Kg): ')))
    keep = str(input('Deseja continuar? [S/N] ')).lower()
    people.append(data[:])
    data.clear()

if len(people) == 1:
    print('Apenas uma pessoa foi cadastrada!')
else:
    print(f'Foram cadastradas {len(people):.0f} pessoas!')

for person in people:
    if person[1] > heaviest:
        heaviest = person[1]
    elif person[1] < lighter or lighter == 0:
        lighter = person[1]

for person in people:
    if person[1] == heaviest:
        heaviest_ones.append(person[0])
    elif person[1] == lighter:
        lighter_ones.append(person[0])

print(f'O maior peso foi de {heaviest}Kg. Peso de {heaviest_ones}')
print(f'O menor peso foi de {lighter}Kg. Peso de {lighter_ones}')
