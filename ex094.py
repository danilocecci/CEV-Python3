comunity = list()
person = dict()
keep = 's'
ages = 0
avg_age = 0
count_female = 0
female_group = list()
count_over_avg = 0
avg_age_group = list()

while keep == 's':
    # nome
    person['name'] = str(input('Nome: '))
    # sexo VALIDAÇÃO
    handle_sex = str(input('Sexo [M/F]: ')).lower()
    while handle_sex != 'm' and handle_sex != 'f':
        handle_sex = str(input('Por favor, digite apenas "M" ou "F": ')).lower()
    person['sex'] = handle_sex
    # idade
    person['age'] = int(input('Idade: '))
    # transferir sem vínculo para a lista :D
    comunity.append(person.copy())
    # continuar VALIDAÇÃO
    keep = str(input('Deseja continuar [S/N]? '))
    while keep != 's' and keep != 'n':
        keep = str(input('Por favor, digite apenas "S" ou "N": '))

# total de pessoas cadastradas
print(f'O total de pessoas cadastradas é de {len(comunity)}')
# media de idade
for person in comunity:
    ages += person['age']
avg_age = ages/len(comunity)
print(f'A média de idade é de {avg_age}')
# mulheres cadastradas
for person in comunity:
    if person['sex'] == 'f':
        count_female += 1
        female_group.append(person['name'])
print(f'Foram cadastradas {count_female} mulher(es) neste grupo: {female_group}')
# lista de pessoas que estão acima da média
for person in comunity:
    if person['age'] > avg_age:
        count_over_avg += 1
        avg_age_group.append(person['name'])
print(f'Há {count_over_avg} pessoa(s) com idade acima da média: {avg_age_group}')
# fim
