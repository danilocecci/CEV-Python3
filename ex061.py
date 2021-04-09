nth_term = int(input('Digite o primeiro termo: '))
common_difference = int(input('Digite a razão: '))
counter = 1
terms = nth_term

while counter <= 10:
    print(terms,end=', ')
    terms += common_difference
    counter += 1
print('Fim')