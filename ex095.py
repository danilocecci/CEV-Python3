table = list()
player = dict()
goals = list()
score = 0
keep = 's'

while keep == 's':
    player['name'] = str(input('Nome do jogador: '))
    player['match'] = int(input(f'Quantas partidas {player["name"]} jogou? '))
    for counter in range(0, player['match']):
        handle_goals = int(input(f'Quantos gols {player["name"]} fez na {counter+1}ª partida? '))
        goals.append(handle_goals)
        score += handle_goals
    player['goals'] = goals[:]
    player['score'] = score
    score = 0
    table.append(player.copy())
    goals.clear()
    keep = str(input('Deseja continuar? [S/N] ')).lower() [0]
    print()

print('-='*10+'-')
print(table)
print('-='*10+'-')

print('cod  ', end='')
for index in player.keys():
    print(f'{index:<15}', end='')
print()
print('-'*30)
for key, value in enumerate(table):
    print(f'{key:>3}  ', end='')
    for d in value.values():
        print(f'{str(d):<15}', end='')
    print()
print()

while True:
    search = int(input('Digite o código do jogador para exibir informações: (999 para sair) '))
    if search == 999:
        break
    if search >= len(table):
        print(f'O código {search} é inexistente. Por favor, digite um código válido!')
    else:
        print(f'DADOS DO JOGADOR: {table[search]["name"]}!'.upper())
        for index, goals in enumerate(table[search]['goals']):
            print(f'    {goals} gols no {index+1}º jogo.')
        print('-'*30)

print('Obrigado :D')