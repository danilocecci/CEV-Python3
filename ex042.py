import colorama
colorama.init()

print('-='*10+'-')
print('\033[1;31m   TRIÂNGULOS V2\033[m')
print('-='*10+'-')

print('Vamos ver se é possível formar um triângulo e que tipo de triângulo é esse.')
side1 = float(input('Digite o valor de um dos lados desse triângulo: '))
side2 = float(input('Digite o valor do outro lado desse triângulo: '))
side3 = float(input('Digite o valor do último lado desse triângulo: '))

if side1 > side2 + side3 or side2 > side1+side3 or side3 > side1 + side2:
    print('Não é possível formar um triângulo com as medidas {}, {} e {}'.format(side1, side2, side3))
else:
    print('É possível formar um triângulo com as medidas {}, {} e {}'.format(side1, side2, side3))
    if side1 == side2 and side1 == side3:
        print('Tipo do triângulo: \033[1mEQUILÁTERO\033[m!')
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print('Tipo do triângulo: \033[1mISÓSCELES\033[m!')
    else:
        print('Tipo do triângulo: \033[1mESCALENO\033[m!')
