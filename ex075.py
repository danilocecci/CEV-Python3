numbers = (int(input('Digite um número inteiro: ')), int(input('Digite o segundo número inteiro: ')), int(input('Digite o terceiro número inteiro: ')), int(input('Digite o quarto e último número inteiro: ')))
nine_counter = 0
even = []

if 9 in numbers:
    nine_counter += 1
    print(f'O número 9 apareceu {nine_counter} vezes.')

if 3 in numbers:
    print(f'O número 3 apareceu na posição {numbers.index(3)+1}!')
else:
    print('O número 3 não apareceu em nenhuma posição!')

for c in range(0,3):
    if numbers[c] % 2 == 0:
        even.append(numbers[c])
print(f'Os números pares foram: {even}')