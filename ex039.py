import colorama, time
colorama.init()

print('-='*10+'-')
print('\033[1;31m EXÉRCITO BRASILEIRO\033[m')
print('-='*10+'-')

year = int(input('Digite o ano de seu nascimento: '))
years_old = int(time.strftime("%Y"))-year

if years_old == 17:
    print('Aliste-se já. Chegou sua hora')
elif years_old < 17:
    print('Calma... Ainda faltam {} ano(s)!'.format(17-years_old))
else:
    print('Vish... já passou o tempo de se alistar. Alegria!')