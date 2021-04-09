import colorama
colorama.init()

print('-='*6+'-')
print('\033[1;31m PALÍNDROMO\033[m')
print('-='*6+'-')

print('Vamos descobrir se sua frase é palíndroma!')

frase = str(input('Digite sua frase abaixo:\n'))
frase_divida = frase.split()
letra = []

for palavra in frase:
    letra += palavra.split()
letra_invertida = letra
letra_invertida.reverse()

if letra == letra_invertida:
    print('Essa frase é palíndroma!')
else:
    print('Essa frase não é palíndroma!')