player = dict()
handle_score = list()

player['name'] = str(input('Nome do jogador: '))
player['games'] = int(input(f"Quantas partidas {player['name']} jogou? "))
for c in range(0,player['games']):
    handle_score.append(int(input(f"Quantos gols {player['name']} fez na {c+1}ª partida? ")))
player['score'] = handle_score
player['scorePoints'] = sum(player['score'])

##Prints 

#Print1
#print(player)

#Print2
# for k,v in player.items():
#    print(f'O campo {k} tem valor {v}')

#Print3
print(f"\nO jogador {player['name']} jogou {player['games']} partidas.")
for c in range(0,len(handle_score)):
    print(f"-Na {c+1}ª partida, fez {handle_score[c]} gols.")
print(f"Foi um total de {player['scorePoints']} gols.")