import colorama
colorama.init()

print('-='*10+'-')
print('\033[1;31mCONVERSOR NUMÉRICO\033[m')
print('-='*10+'-')

number = int(input('Digite um número inteiro: '))
choice = int(input('Agora digite o número de alguma das opções a seguir:\n1 - Converter para binário\n2 - Converter para octal\n3 - Converter para hexadecimal\nSua escolha: '))

if choice == 1:
    print(bin(number))
elif choice == 2:
    print(oct(number))
elif choice == 3:
    print(hex(number))
else:
    print('Você não escolheu uma opção válida!')