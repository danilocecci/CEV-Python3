answer = 'm'
aged = 0
male = 0
young_female = 0
sex = 'd'
age = 2

while answer.lower() != 'n':
    answer = 'm'
    sex = 'd'
    age = 2
    
    print('\n'+'-='*10+'-')
    print('CADASTRE UMA PESSOA')
    print('-='*10+'-')

    while sex.lower() != 'm' and sex.lower() != 'f':
        sex = input('Digite seu sexo [M/F]: ')
    
    while True:
        try:
            age = int(input('Digite sua idade: '))
        except ValueError:
            continue
        else:
            break
        
    while answer.lower() != 's' and answer.lower() != 'n':
        answer = input('Deseja continuar [S/N]: ')

    if age > 18:
        aged += 1
    
    if sex.lower() == 'm':
        male += 1
    
    if sex.lower() == 'f' and age < 20:
        young_female += 1

print('\nRESULTADO:')
print('Foram cadastradas {} pessoas com idade superior a 18 anos.'.format(aged))
print('Foram cadastrados {} homens.'.format(male))
print('Foram cadastradas {} mulheres com idade inferior a 20 anos.'.format(young_female))