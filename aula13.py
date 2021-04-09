init = int(input('Início: '))
final = int(input('Final: '))
jump = int(input('Passo: '))

for c in range(init, final+1, jump):
    print(c)
print('FIM!')