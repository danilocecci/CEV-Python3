import colorama, time, random
colorama.init()

print('-='*5+'-')
print('\033[1;31m  JOKENPÔ \033[m')
print('-='*5+'-')

print('Hora da diversão!\n')

human_choice = int(input('Escolha sua jogada:\n1 - Pedra;\n2 - Papel;\n3 - Tesoura.\nRESPOSTA: '))
machine_choice = random.randint(1,3)
choices = ['Pedra', 'Papel', 'Tesoura']


print('Minha escolha foi {}!'.format(choices[machine_choice-1]))

if human_choice == machine_choice:
    time.sleep(1)
    print('Pensamos iguais! Empatou.')
elif human_choice == 1 and machine_choice == 2:
    time.sleep(1)
    print('Ganhei de você! Papel ganha de Pedra!')
elif human_choice == 2 and machine_choice == 1:
    time.sleep(1)
    print('Parabéns, você me venceu! Papel ganha de Pedra!')
elif human_choice == 2 and machine_choice == 3:
    time.sleep(1)
    print('Ganhei de você! Tesoura ganha de Papel!')
elif human_choice == 3 and machine_choice == 2:
    time.sleep(1)
    print('Parabéns, você me venceu! Tesoura ganha de Papel!')
elif human_choice == 3 and machine_choice == 1:
    time.sleep(1)
    print('Ganhei de você! Pedra ganha de Tesoura!')
elif human_choice == 1 and machine_choice == 3:
    time.sleep(1)
    print('Parabéns, você me venceu! Pedra ganha de Tesoura!')
else:
    time.sleep(1)
    print('Poxa... você não sabe brincar!')