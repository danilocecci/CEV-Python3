from math import sin, cos, tan
angle = float(input('Digite um ângulo qualquer: '))
seno = sin(angle)
coseno = cos(angle)
tangente = tan(angle)
print('O seno de {0:.2f} é {1:.2f}.\nO coseno de {0:.2f} é {2:.2f}.\nA tangente de {0:.2f} é {3:.2f}'.format(angle, seno, coseno, tangente))