import colorama
colorama.init()

print('-='*10+'-')
print('\033[1;31m O GORDO E O MAGRO!\033[m')
print('-='*10+'-')

print('Medindo 5 pessoas para descobrir quem é o mais gordinho e o mais magrinho :D')

pesos = []

for c in range(1,6):
    pesos.append(float(input('Digite o peso (KG) da {}ª pessoa: '.format(c))))

print('\nA pessoa mais gordinha pesa {:.2f}KG e a mais magrinha pesa {:.2f}KG! :D'.format(max(pesos),min(pesos)))