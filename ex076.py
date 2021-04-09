print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

products = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.90)

for product in range(0, len(products)):
    if product % 2 == 0:
        print(f'{products[product]:.<25}', end='')
    else:
        print(f'R${products[product]:>8.2f}')

print('-'*40)