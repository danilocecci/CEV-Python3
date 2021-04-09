import colorama, time
colorama.init()

print('-='*5+'-')
print('\033[1;31m   I.M.C.\033[m')
print('-='*5+'-')

print('Vamos calcular seu Índice de Massa Corpórea!')

weight = float(input('Digite seu peso(KG) : '))
height = float(input('Digite sua altura(m) : '))
imc = weight/pow(height,2)

print('Seu IMC é {:.1f}!'.format(imc))

if imc < 18.5:
    print('\033[31mVocê está abaixo do peso ideal!\033[m')
elif imc >= 18.5 and imc <= 25:
    print('\033[32mVocê está no peso ideal!\033[m')
elif imc >= 26 and imc <=30:
    print('\033[31mVocê está com sobrepeso!\033[m')
elif imc >= 31 and imc <= 40:
    print('\033[31mVocê está com obesidade!\033[m')
else:
    print('\033[31mVocê está com obesidade mórbida!\033[m')

print('Obrigado por utilizar uma ferramenta desenvolvida pelo Danilo :D')

time.sleep(5)