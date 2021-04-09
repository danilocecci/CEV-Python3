number = int((input('Digite um número inteiro para saber seu fatorial: ')))
counter = number
fatorial = 1
while counter >= 1:
    fatorial *= counter
    counter -= 1

print('O fatorial de {} é igual a {}'.format(number, fatorial))

''' -=Foi recomendado tentar juntamente com o FOR!=-
fatorial_for = 1
for c in range(number,1,-1):
    fatorial_for *= c
print('O fatorial de {} é igual a {}'.format(number, fatorial_for))
'''
