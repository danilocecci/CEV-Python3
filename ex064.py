numbers = []

numbers.append(int(input('Digite um número inteiro: ')))

while 999 not in numbers:
    numbers.append(int(input('\nSe quiser sair, digite 999\nSe deseja continuar, digite outro número inteiro!\nSUA RESPOSTA: ')))

numbers.remove(999)
print('\nEstes foram os números que você digitou: {}.'.format(numbers))
print('Você digitou {} números.'.format(len(numbers)))
print('A soma desses números é igual a {}.'.format(sum(numbers)))
