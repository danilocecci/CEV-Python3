nth_term = int(input('Digite o primeiro termo: '))
common_difference = int(input('Digite a razão: '))
counter = 1
terms = nth_term

while counter <= 10:
    print(terms,end=', ')
    terms += common_difference
    counter += 1
print('FIM\n')
counter = 1

more_terms = int(input('Deseja que calcule mais termos?\nDigite "0" se NÃO\nDigite a quantidade de termos a mais que desejar!\nRESPOSTA: '))

while more_terms != 0:
    while counter <= more_terms:
        print(terms, end=', ')
        terms += common_difference
        counter += 1
    print('FIM\n')
    counter = 1
    more_terms = int(input('Deseja que calcule mais termos?\nDigite "0" se NÃO\nDigite a quantidade de termos a mais que desejar!\nRESPOSTA: '))
print('Obrigado!')
