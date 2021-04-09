from random import shuffle
equipe1 = input('Digite o nome da equipe1: ')
equipe2 = input('Digite o nome da equipe2: ')
equipe3 = input('Digite o nome da equipe3: ')
equipe4 = input('Digite o nome da equipe4: ')
shuff = [equipe1,equipe2, equipe3, equipe4]
shuffle(shuff)
print('A ordem das equipes ficou assim: {}'.format(shuff))