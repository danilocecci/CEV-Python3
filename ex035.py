line1 = int(input('Digite um número inteiro: '))
line2 = int(input('Digite outro número inteiro: '))
line3 = int(input('Digite mais um número inteiro: '))
if line1 >= (line2 + line3) or line2 >= (line1 + line3) or line3 >= (line1 + line2):
    print('Não é possível formar um triângulo com as medidas "{}", "{}" e "{}"'.format(line1, line2, line3))
else:
    print('É possível formar um triângulo com as medidades "{}", "{}" e "{}!'.format(line1, line2, line3))
