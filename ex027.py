nome = input('Digite seu nome completo: ')
nome_splitado = nome.strip().split()
print('Seu primeiro nome é {}!\nE o último nome é {}!'.format(nome_splitado[0], nome_splitado[-1]))