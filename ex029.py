from time import sleep

velocity = float(input('Sabendo que a velocidade máxima permitida é de 80km/h, a que velocidade (KM/h) você deseja andar nessa via? '))
print('Ok! Boa viagem. :D')
sleep(1)
if velocity > 80.0:
    print('O oh... Uma multa foi registrada em seu nome. O valor foi de R${:.2f}'.format((velocity-80)*7))
else:
    print('Ah... e parabéns pela boa conduta ao volante! :D')
    