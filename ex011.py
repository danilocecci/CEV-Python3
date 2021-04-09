print('')
print('Olá. Agora vamos calcular a área de uma parede e a quantidade de tinta pintá-la!')
width = float(input('Por favor, digite a largura da parede em Metros: '))
print('Obrigado!')
height = float(input('Agora digite a altura da parede em Metros: '))
area = width * height
print('')
print('A área da parede informada é de {:.2f}m². E quantidade de tinta utilizada será de {:.2f}l!'.format(area, (area/2)))