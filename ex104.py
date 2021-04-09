#Desafio 104 - Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n=leiaInt('digite um n')

def leiaInt(userInput):
    isNum = input(userInput)
    while isNum.isnumeric() != True:
        print(f'ERRO! Digite um número inteiro válido!')
        isNum = input(userInput)
    else:
        return isNum

isNum = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {isNum}!')