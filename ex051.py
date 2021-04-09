import colorama
colorama.init()

print('-==-')
print('\033[1;31m PA\033[m')
print('-==-')

print('Mostrando os 10 primeiros termos de uma Progressão Aritimética!')

start = int(input('Digite o primeiro termo: '))
jump = int(input('Digite a razão: '))
dec = start + (10 - 1 ) * jump

for c in range(start,dec + jump,jump):
    print(c,end=' ► ')
print('FIM')