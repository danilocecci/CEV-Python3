#Desafio 113 - Reescreva função leiaInt() que fizemos no #Desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(userInput):
    while Exception:
        try:
            handleInt = int(input(userInput))
        except ValueError:            
            print(f'ERRO! Você não digitou um número inteiro.')
        except KeyboardInterrupt:
            print('Ok...')
            return 0
        else:
            return handleInt

def leiaFloat(userInput):
    while Exception:
        try:
            handleFloat = float(input(userInput))
        except ValueError:
            print(f'ERRO! Você não digitou um número real!')
        except KeyboardInterrupt:
            print('Ok...')
            return 0
        else:
            return handleFloat


handleInt = leiaInt('Digite um número inteiro: ')
handleFloat = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {handleInt} e o real foi {handleFloat}!')
