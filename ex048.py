import colorama
colorama.init()

print('-='*8+'-')
print('\033[1;31m MÚLTIPLOS DE 3! \033[m')
print('-='*8+'-')

print('Mostrando a soma todos os números ímpares que são múltiplos de três no intervalo de 1 até 500!\n')

counter = 0

for c in range(1,501):
    if c%3 == 0 and c%2 != 0:
        counter += c
print('RESPOSTA: {}'.format(counter))