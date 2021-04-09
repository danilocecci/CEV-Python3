# #interactive help - Manual
# help(input) #método1
# print(input.__doc__) #método2

# #DocStrings - Uma string de documentação de uma função própria
# def contador(i, f, p):
#     """
#     Faz uma contagem e mostra na tela.
#     :param i: início da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     Função criada por Gustavo Guanabara do canal CursoemVideo (realmente é dele, só copiei pra estudar :D)
#     """
#     c = i
#     while c <= f:
#         print(f'{c}',end='..')
#         c += p
#     print('FIM!')
# contador(2,10,2)
# # help(contador) ??
# help(contador)

# #Parâmetros opicionais - Deixar parâmetros pré definidos, caso o usuário não preencher a variável, o código executa sem nenhum problema :D
# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     print(f'A soma vale {s}')

# somar(3,2,5)
# somar(1)
# somar(1,6)

# #Escopo de variáveis - Local onde uma variável vai existir ou não :D
# #Escopo global e escopo local.
# def funcao():
#     global n1
#     n1 = 4
#     print(f'N1 dentro vale {n1}')

# n1 = 2
# funcao()
# print(f'N1 global vale {n1}')

#Retorno de valores - Funções no Python podem não retornar (imprimir dentro delas) ou retornar um valor. (RETURN)
def somar(a=0,b=0,c=0):
    s=a+b+c
    #print(f'A soma vale {s}')
    return s
r1 = somar(3,2,5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Meus cálculos deram {r1}, {r2} e {r3}!')