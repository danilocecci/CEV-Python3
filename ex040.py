import colorama
colorama.init()

print('-='*10+'-')
print('\033[1;31m   PASSEI DE ANO?\033[m')
print('-='*10+'-')

grade1 = float(input('Digite a sua primeira nota: '))
grade2 = float(input('Digite a sua segunda nota: '))
average = (grade1+grade2)/2

print('MÉDIA: {}'.format(average))

if average < 5.0:
    print('STATUS: \033[31mREPROVADO\033[m!')
elif average >=5.0 and average <= 6.9:
    print('STATUS: EM RECUPERAÇÃO!')
else:
    print('STATUS: APROVADO!')
