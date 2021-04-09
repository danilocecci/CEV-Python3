from time import sleep

def counter(start, end, step):
    if step == 0:
        step = 1
    if start < end:
        print(f'Contando de {start} até {end} de {step} em {step}.')
        sleep(2)
        while start <= end:
            print(start, end='-> ', flush=True)
            sleep(0.3)
            start += step
        print('FIM')
    elif start > end:
        print(f'Contando de {start} até {end} de {abs(step)} em {abs(step)}.')
        sleep(2)
        if step < 0:
            while start >= end: 
                print(start, end='-> ', flush=True)
                sleep(0.3)
                start += step
        else:
            while start >= end: 
                print(start, end='-> ', flush=True)
                sleep(0.3)
                start -= step
        print('FIM')
    else:
        print('Os números são iguais. Você quer quebrar o jogo? Isso me deixa triste. \nPara rodar novamente, você deverá reiniciar o programa.')
        sleep(2)


counter(1, 10, 1)
counter(10, 0, 2)
userCountStart = int(input('Número inicial da contagem: '))
userCountEnd = int(input('Número final da contagem: '))
userCountStep = int(input('Passo da contagem: '))
counter(userCountStart, userCountEnd, userCountStep)
sleep(2)