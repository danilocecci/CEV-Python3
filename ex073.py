teams = ('Atlético-MG', 'Internacional', 'Palmeiras', 'Flamengo', 'São Paulo', 'Vasco da Gama', 'Fluminense', 'Sport Recife', 'Santos', 'Fortaleza', 'Athetico-PR', 'Ceará SC', 'Corinthians', 'Atlético-GO', 'Grêmio', 'Bahia', 'Coritiba', 'Bragantino-SP', 'Botafogo', 'Goiás')
searched_team = 'Palmeiras'
print('BRASILEIRÃO')
print(f'Os cincos primeiros colocados são: {teams[:5]}')
print(f'\nOs últimos 4 colocados da tabela são: {teams[-4:len(teams)]}')
print(f'\nA lista em ordem alfabética fica: {sorted(teams)}')
print(f'\nPalmeiras está na {teams.index(searched_team)+1}ª colocação!')