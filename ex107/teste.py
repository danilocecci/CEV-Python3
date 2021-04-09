import moeda

userInput = float(input('Digite o preço: R$'))
print(f'O dobro de {userInput} é {moeda.dobro(userInput)}!')
print(f'A metade de {userInput} é {moeda.metade(userInput)}!')
print(f'Aumentando 10%, temos {moeda.aumentar(userInput,10)}!')
print(f'Reduzindo 13%, temos {moeda.diminuir(userInput,13)}!')