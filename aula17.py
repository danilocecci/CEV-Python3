##Tupla
#num = (2, 5, 9, 1)
#num[2] = 3
#print(num)

#Lista
# num = [2, 5, 9, 1]
# num[2] = 3
# num.append(7)
# #num.sort()
# num.sort(reverse=True)
# num.insert(2, 0)
# num.pop(2)
# if 5 in num:
#     num.remove(5)
# else:
#     print('Não encontrei o 5')
# print(num)
# print(f'Essa lista tem {len(num)} elementos.')

##Testando append, indexes e valores.
# valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)

# for c,v in enumerate(valores):
#     print(f'Na posição {c+1} encontrei o valor {v}!')
# print('Cheguei ao final da lista.')

##Ler valores e inserí-los na lista
# valores = list()
# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))
# for c,v in enumerate(valores):
#     print(f'Na posição {c+1} encontrei o valor {v}!')
# print('Cheguei ao final da lista.')

a = [2, 3, 4, 7]
#ligação de 'b' e 'a'
#b = a

#sem ligação, apenas pegando os valores :D
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')