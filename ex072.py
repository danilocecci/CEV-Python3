extended_number = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

number = int(input('Digite um número entre 0 e 20: '))

while number < 0 or number > 20:
    number = int(input('Número inválido! Digite um número entre 0 e 20: '))

print(f'Você digitou o número {extended_number[number]}!')