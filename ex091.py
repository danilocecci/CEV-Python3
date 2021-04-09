from random import randint
from time import sleep
from operator import itemgetter

players = {
    'Player1': randint(1,6),
    'Player2': randint(1,6),
    'Player3': randint(1,6),
    'Player4': randint(1,6),
}

ranking = list()

print('Random values:')
for key, value in players.items():
    print(f'{key} randomized {value} on dice.')
    sleep(1)

ranking = sorted(players.items(), key = itemgetter(1), reverse=True)
print('-='*20+'-')
for index, value in enumerate(ranking):
    print(f'{index+1}º place: {value[0]} with {value[1]} points.')
