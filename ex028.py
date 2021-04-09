from random import randint
from time import sleep

number = randint(0,5)
choice = int(input('Escolha um número entre 0 e 5: '))
print('Processando...')
sleep(1)
if choice == number:
    print('Parabéns, você acertou! Eu estava mesmo pensando no número {}!'.format(number))
else:
    print('Que pena. Não estamos na mesma sintonia. Eu tinha pensando no número {}.'.format(number))