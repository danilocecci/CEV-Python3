from time import sleep

withdraw_value = int(input('Digite o valor a ser sacado: R$'))
print('Ok. Calculando notas...\n')
sleep(1)
money = 0
note_50 = 0
note_20 = 0
note_10 = 0
note_1 = 0

while withdraw_value != 0:
    while withdraw_value >= 50:
        money += 50
        withdraw_value -= 50
        note_50 += 1
    while withdraw_value >= 20:
        money += 20
        withdraw_value -= 20
        note_20 += 1
    while withdraw_value >= 10:
        money += 10
        withdraw_value -= 10
        note_10 += 1
    while withdraw_value >= 1:
        money += 1
        withdraw_value -= 1
        note_1 += 1
    
print('Foram {} notas de R$50,00\nForam {} notas de R$20,00\nForam {} notas de R$10,00\nForam {} notas de R$1,00'.format(note_50,note_20,note_10,note_1))
print('Totalizando a quantia de R${},00 retirada!\nObrigado :D '.format(money))