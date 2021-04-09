import colorama
colorama.init()

print('-='*7+'-')
print('\033[1;31m NÚMEROS PARES \033[m')
print('-='*7+'-')

print('Mostrando números pares de 0 a 50!\n')

for c in range(1,51):
    if c%2 == 0:
        print(c)
