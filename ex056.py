import colorama, time
colorama.init()

print('-='*6+'-')
print('\033[1;31mESTATÍSTICAS\033[m')
print('-='*6+'-')

print('Após informar os dados de 4 pessoas, vou retornar a \033[33mMÉDIA DE IDADE\033[m, o \033[33mHOMEM MAIS VELHO\033[m e quantas \033[33mMULHERES\033[m tem \033[33mMENOS DE 20 ANOS\033[m!')

name = []
age = []
sex = []
age_male = []
youngs_female = 0

for c in range(1,5):
    print('')
    print('-='*6+' {}ª Pessoa '.format(c)+'-='*6+'-')
    name.append(input('Digite o nome da {}ª pessoa: '.format(c)))
    age.append(int(input('Agora, digite a idade dessa pessoa: ')))
    sex.append(input('E por fim, digite o sexo dessa pessoa: '))
    if sex[c-1] == 'Masculino' or sex[c-1] == 'M' or sex[c-1] == 'Masc' or sex[c-1] == 'Masc.':
        age_male.append(age[c-1])
    elif sex[c-1] == 'Feminino' or sex[c-1] == 'F' or sex[c-1] == 'Fem' or sex[c-1] == 'Fem.':
        if age[c-1] < 20:
            youngs_female += 1
time.sleep(1)
print('Obrigado!')
time.sleep(1)

print('Vamos às respostas!')
print('A média de idade do grupo é de {} anos!'.format(sum(age)/len(age)))
time.sleep(1)
print('O homem mais velho é o {}!'.format(name[age_male.index(max(age_male))]))
time.sleep(1)
print('Nesse grupo há {} mulheres menores de 20 anos de idade! :D'.format(youngs_female))
print('')
time.sleep(1)
print('Obrigado por utilizar mais uma ferramenta de Danilo :D')