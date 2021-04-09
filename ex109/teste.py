import moeda

userInput = float(input('Digite o preço: R$'))
print(f'O dobro de {moeda.moeda(userInput)} é {moeda.dobro(userInput, True)}!')
print(f'A metade de {moeda.moeda(userInput)} é {moeda.metade(userInput, True)}!')
print(f'Aumentando 10%, temos {moeda.aumentar(userInput,10, True)}!')
print(f'Reduzindo 13%, temos {moeda.diminuir(userInput,13, True)}!')