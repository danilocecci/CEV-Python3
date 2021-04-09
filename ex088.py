from random import randint
from time import sleep

games = list()
quantity = int(input('Deseja quantos palpites de jogos? R: '))

for c in range(0,quantity):
    for x in range(0,6):
        handle_num = randint(1,60)
        while handle_num in games:
            handle_num = randint(1,60)
        games.append(handle_num)
    games.sort()
    print(f'Jogo {c+1}: {games}')
    games.clear()
    sleep(1)