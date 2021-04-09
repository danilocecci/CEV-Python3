def area(width, lenght):
    area = width * lenght
    print(f'A área de um terreno {width}x{lenght}m é de {area}m².')

print()
print('Controle de Terrenos')
print('---------------------')

width = float(input('LARGURA (m): '))
length = float(input('COMPRIMENTO (m): '))

area(width,length)