phrase = input('Diga alguma coisa: ')
count_a = phrase.lower().count('a')
print('A letra "A" pareceu {} vezes'.format(count_a))
print('A primeira letra A foi a {}ª letra a ser digitada!'.format(phrase.lower().find('a')+1))
print('A última letra A foi do caractere nº{}'.format(phrase.lower().rfind('a')+1))