numbers = []

numbers.append(int(input('Digite um número inteiro: ')))
wanna_play = int(input('\nDeseja continuar?\n[1] SIM.\n[2] NÃO.\nSUA RESPOSTA: '))

while wanna_play == 1:
    numbers.append(int(input('\nDigite outro número inteiro: ')))
    wanna_play = int(input('\nDeseja continuar?\n[1] SIM.\n[2] NÃO.\nSUA RESPOSTA: '))

print('\nVamos aos resultados:')
print('Os números digitados foram: {}.'.format(numbers))
print('A média entre todos os valores é de {:.2f}.'.format(sum(numbers)/len(numbers)))
print('O MENOR número digitado foi: {}.'.format(min(numbers)))
print('O MAIOR número digitado foi: {}.'.format(max(numbers)))
