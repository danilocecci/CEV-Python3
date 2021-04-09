choices = 0
sum_choices = 0

while True:
    choice = int(input('Digite um número (999 para parar): '))
    if choice == 999:
        break
    sum_choices += choice
    choices += 1

print(f'A soma dos {choices} valores foi {sum_choices}!')