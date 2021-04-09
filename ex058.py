from random import randint

counter = 1
bot_pick = randint(0,10)
print('Pensei em um número entre 0 e 10. Tente adivinhar!')
player_pick = int(input('Chute um número: '))

while player_pick != bot_pick:
    player_pick = int(input('Chute outro número: '))
    counter += 1
print('Parabéns! Você adivinhou meu número em {} tentativas!'.format(counter))