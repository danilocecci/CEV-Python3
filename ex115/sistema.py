from lib.interface import *
from lib.arquivo import *
from time import sleep
import os

file = os.path.join(pathlib.Path(__file__).parent.absolute(),'cursoemvideo.txt')
if not isFile(file):
    createFile(file)

while True:
    answer = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if answer == 1:
        readFile(file)
    elif answer == 2:
        cabecalho('NOVO CADASTRO')
        name = str(input('Nome: '))
        age = leiaInt('Idade: ')
        register(file, name, age)
    elif answer == 3:
        print('Saindo do sistema... Obrigado e volte sempre!')
        sleep(2)
        break
    else:
        print('ERRO! Digite uma opção válida!')
    sleep(2)