import colorama
colorama.init()

print('-='*10+'-')
print('\033[1;31m   MAIOR >< MENOR\033[m')
print('-='*10+'-')

number1 = int(input('Digite um número inteiro: '))
number2 = int(input('Digite um número inteiro: '))

if number1>number2:
    print('O primeiro valor é o maior.')
elif number2>number1:
    print('O segundo valor é o maior.')
else:
    print('Não existe valor maior, os dois são iguais.')