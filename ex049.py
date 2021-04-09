import colorama
colorama.init()

print('-='*5+'-')
print('\033[1;31mTABUADA V2\033[m')
print('-='*5+'-\n')

number = int(input('Digite um número inteiro para montar a tabuada: '))

for c in range(0,11):
    print('{} x {} = {}'.format(number, c, number*c))
print('Obrigado por utilizado mais uma ferramenta de Danilo :D')
