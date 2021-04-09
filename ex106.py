#Desafio 106 - Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. OBS.: use cores
import colorama
from time import sleep
colorama.init()

def HelPy():
    userInput = 'oi'
    while userInput != 'fim':
        sleep(1)
        Cabecalho()
        sleep(2)
        userInput = str(input('Função ou Biblioteca > ')).lower()
        if userInput == 'fim':
            break
        print(f"Acessando o manual do comando '{userInput}'." )
        sleep(1)
        print(colorama.Back.CYAN)
        print(help(userInput))
        print(colorama.Style.RESET_ALL)
    print(f'Saindo do HelPy. Obrigado por usar uma ferramenta do Danilo Cecci :D')
    sleep(3)

def Cabecalho():
    print(colorama.Back.GREEN + f'-='*12+'-')
    print(f'Sistema de ajuda HelPy!')
    print(f'-='*12+'-')
    print(colorama.Style.RESET_ALL)


HelPy()