from math import hypot
catadj = int(input('Informe o valor inteiro do comprimento do cateto adjacente: '))
catopo = int(input('Informe o valor inteiro do comprimento do cateto oposto: '))
hypo = hypot(catadj,catopo)
print('O valor da hipotenusa é {:.2f}!'.format(hypo))
