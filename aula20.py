#funções - ROTINAS
# def makeLine(text):
#     length = len(text)
#     print('-='*(length*2)+'-')
#     print(text.center(length*4))
#     print('-='*(length*2)+'-')
# def soma(a,b):
#     print(f'A soma de {a} e {b} é igual a {a+b}!')


# text = input('Digite um texto para testar a aula: ')
# makeLine(text)
# print()

# wannaSum = input('Digite "SIM" para fazer uma soma ou qualquer outra coisa para fechar o programa: ')
# if wannaSum.upper() == 'SIM':
#     a = int(input('Digite o primeiro número da soma: '))
#     b = int(input('Digite o segundo número da soma: '))
#     soma(a,b)
# print('Obrigado :D')
# if wannaSum.upper() != 'SIM':
#     print('Ok, sem soma alguma!')

# #práticas
# def somatoria(a,b):
#     print(f'O valor de A = {a} e de B = {b}')
#     resultado = a + b
#     print(f'O resultado dessa soma é igual a {resultado}')


# somatoria(b=4,a=5)
# somatoria(7, 2)

# def contador(* num):
#     print('Você me deu',len(num), 'números:',end=" ")
#     for valor in num:
#         print(f'{valor}',end=" ")

# contador(8,2, 1, 3)

# def dobra(list):
#     pos = 0
#     while pos < len(list):
#         list[pos] *= 2
#         pos += 1

# valores = [6, 4, 2, 1, 3, 9]
# dobra(valores)
# print(valores)

def soma(* valores):
    soma = 0
    for num in valores:
        soma += num
    print(f'Somando os valores {valores} temos {soma}')

soma(5, 2)
soma(2, 9 , 4)