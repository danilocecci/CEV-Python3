import colorama
colorama.init()

print('-='*4+'-')
print('\033[1;31m SOMA-SE\033[m')
print('-='*4+'-')

result_even = 0
result_odd = 0
numbers = [1,2,3,4,5,6]

for c in range(1,7):
    number = int(input('\nEtapa ({}/6)\nDigite um número inteiro para efetuar a soma: '.format(c)))
    numbers[c-1] = number
    if number%2 == 0:
        result_even += number
    else:
        result_odd += number
print('\nNúmeros recebidos: {}\nSoma dos pares: {}\nSoma dos ímpares: {}'.format(numbers,result_even,result_odd))