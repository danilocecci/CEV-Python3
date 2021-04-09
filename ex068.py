from random import randint

print('-='*12+'-')
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*12+'-')

total_wins = 0

while True:
    human_value = int(input('Digite um valor inteiro: '))
    side = input('Par ou Ímpar? [P/I] ')
    machine_value = randint(0, 10) 
    sum_values = human_value + machine_value
    
    def what_side(sum_values):
        if sum_values % 2 == 0:
            return 'PAR'
        else:
            return 'IMPAR'

    def is_correct(sum_values, side):
        if (sum_values % 2 == 0 and side == 'p') or (sum_values % 2 != 0 and side == 'i'):
            return True
        else:
            return False

    print('-='*12+'-')
    print('Você jogou {} e a máquina jogou {}. Total de {} DEU {}!'.format(human_value, machine_value, sum_values, what_side(sum_values)))
    
    if is_correct(sum_values, side) != True:
        break
    else:
        total_wins += 1

print('-='*6+'-')
print('VOCÊ PERDEU!')
print('-='*6+'-')
print('GAME OVER!\nVocê venceu {} vezes.'.format(total_wins))
