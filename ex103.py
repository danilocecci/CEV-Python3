#Desafio 103 - Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def card(name,goals):
    """f: card(name,goals) - Pega o nome e a quantidade de gols

    Args:
        name (str): Nome do jogador
        goals (int): Quantos gols o jogador marcou
    """
    print(f'O jogador {name} fez {goals} gol(s) no campeonato.')

name = str(input('Digite o nome do jogador: '))
if name.strip() == "" or not name:
    name = '<desconhecido>'
goals = str(input('Digite o número de gols: '))
if goals.isnumeric() == False or not goals:
    goals = 0
    
card(name,goals)