while True:
    number_of_choice = int(input('\nQuer ver a tabuada de qual valor? '))
    if number_of_choice < 0:
        break
    for c in range(1, 11):
        print(f'{number_of_choice} X {c} = {number_of_choice*c}')

print('PROGRAMA TABUADA ENCERRADO. Volte Sempre! Obrigado :D')