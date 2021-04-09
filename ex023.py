number = input('Entre 0 e 9999, digite qualquer número inteiro: ')
casas = len(number)
print(casas)
for i in range (1, casas+1):
    print('A {}ª casa é: {}'.format(i,number[casas-i]))
    i = i + 1
    