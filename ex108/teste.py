import moeda

userInput = float(input('Digite o preço: R$'))
print(f'O dobro de {moeda.moeda(userInput)} é {moeda.moeda(moeda.dobro(userInput))}!')
print(f'A metade de {moeda.moeda(userInput)} é {moeda.moeda(moeda.metade(userInput))}!')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(userInput,10))}!')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(userInput,13))}!')