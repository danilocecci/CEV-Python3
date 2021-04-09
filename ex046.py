from time import sleep
import colorama
colorama.init()

print('-='*5+'-')
print('\033[1;31m ANO NOVO! \033[m')
print('-='*5+'-')

print('Conte comigo para a virada do ano novo!\n')

for c in range(10, 0, -1):
    print(c)
    sleep(1)

print('FELIZ ANO NOVOO!')
sleep(1)
