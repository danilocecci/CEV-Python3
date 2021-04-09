#Tuplas são imutáveis
##lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')

'''for comida in lanche:
    print(f'Eu vou comer {comida}!')
'''

'''for contador in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[contador]}!')
'''

'''for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao}')
'''
##print('Comi pra caramba :D')
##print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a

print()
print(f'Tupla c = {c}')
print(f'O tamanho da tupla c é de {len(c)} itens!')
print(f'O número 5 aparece {c.count(5)}x nessa tupla!')
print()
print(f'Tupla d = {d}')
print(f'O tamanho da tupla d é de {len(d)} itens.')
print(f'O número 2 aparece {d.count(2)}x nessa tupla.')