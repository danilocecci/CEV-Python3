import colorama, time
colorama.init()

print('-='*10+'-')
print('\033[1;31m  P.A.G.A.M.E.N.T.O\033[m')
print('-='*10+'-')

print('Vamos calcular suas condições de pagamento!\n')

normal_price = float(input('Digite o valor do produto: R$'))
payment = int(input('\nDigite a opção correta para a forma de pagamento:\n1 - Pagamento à vista no dinheiro/cheque;\n2 - Pagamento à vista no cartão de crédito;\n3 - Pagamento em até 2x no cartão de crédito;\n4 - Pagamento em 3x ou mais no cartão de crédito.\n\nRESPOSTA: '))

if (payment == 1):
    final_price = normal_price - normal_price*10/100
    print('')
    print('Calculando preço final através do método: Pagamento à vista no dinheiro/cheque...\n')
    time.sleep(2)
    print('Seu preço final ficou em \033[31mR${:.2f}\033[m!'.format(final_price))
elif payment == 2:
    final_price = normal_price - normal_price*5/100
    print('')
    print('Calculando preço final através do método: Pagamento à vista no cartão de crédito...\n')
    time.sleep(2)
    print('Seu preço final ficou em \033[31mR${:.2f}\033[m!'.format(final_price))
elif payment == 3:
    final_price = normal_price
    print('')
    print('Seu preço final ficou inalterado, ou seja, \033[31mR${:.2f}\033[m!'.format(final_price))
elif payment == 4:
    final_price = normal_price + normal_price*20/100
    print('')
    print('Calculando preço final através do método: Pagemento em 3x ou mais no cartão de crédito...')
    time.sleep(2)
    print('Seu preço final ficou com 20% de juros, resultando em \033[31mR${:.2f}\033[m!'.format(final_price))
else:
    print('Não tente quebrar o código!\nDessa vez vou apenas ignorar.')

print('\nObrigado por utilizar mais um sistema do Danilo :D')