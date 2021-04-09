sex = input('Digite seu sexo (M/F): ').upper()

while sex != 'M' and sex != 'F':
    print('Sexo inválido!')
    sex = input('Digite seu sexo (M/F): ').upper()

print('Obrigado!')