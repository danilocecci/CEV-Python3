# teste = list()
# teste.append('Gustavo')
# teste.append(40)
# galera = list()
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])

# print(galera)

# galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# print(galera[2][1])
# for pessoa in galera:
#     print(f'{pessoa[0]} tem {pessoa[1]} anos de idade!')

galera = list()
dado = list()
total_maior_de_idade = total_menor_de_idade = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

# print(galera)
for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade.')
        total_maior_de_idade += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        total_menor_de_idade += 1
print(f'Temos {total_maior_de_idade} maiores de idade e {total_menor_de_idade} menor de idade.')


