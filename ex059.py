pick = 0
first_number = int(input('Digite um número inteiro: '))
second_number = int(input('Digite outro número inteiro: '))
while pick != 5:
    pick = int(input('\nBem vindo ao menuzão! Escolha uma opção:\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair do programa\nOPÇÃO:'))
    print()
    if pick == 1:
        sum = first_number + second_number
        print('A soma de {} e {} é igual a {}'.format(first_number,second_number,sum))
    elif pick == 2:
        multiply = first_number * second_number
        print('A multiplicação entre {} e {} é igual a {}'.format(first_number, second_number, multiply))
    elif pick == 3:
        greater = max(first_number, second_number)
        print('O maior número digitado foi {}'.format(greater))
    elif pick == 4:
        first_number = int(input('Digite um número inteiro: '))
        second_number = int(input('Digite outro número inteiro: '))            
print('Obrigado! :D')