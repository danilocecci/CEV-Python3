again = 's'
product = ''
product_price = 0
total_price = 0
expensives = 0
lower_price = 9999999999999
lower_price_product = 'oi'

while again.lower() == 's':
    print('\n CADASTRANDO PRODUTOS')

    product = input('Digite o nome do produto: ')
    product_price = float(input('Digite o preço desse produto: '))

    total_price += product_price

    if product_price > 1000:
        expensives += 1
    
    if product_price < lower_price:
        lower_price = product_price
        lower_price_product = product

    again = input('Próximo produto [S/N]? ').lower()

print('\nO total gasto nessa compra foi de R${:.2f}!'.format(total_price))
print('{} produtos custaram mais de R$1000,00!'.format(expensives))
print('O produto mais barato foi "{}" e custou R${:.2f}!'.format(lower_price_product,lower_price))