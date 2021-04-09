print('Agora vamos de tabuada!')
numero = int(input('Para isso, preciso que escolha algum número para calcular a tabuada: '))
for i in range(11):
    print('{} x {} = {}'.format(numero, i, (numero*i)))