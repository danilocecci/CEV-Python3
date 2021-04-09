cidade = input('Digite o nome da sua cidade: ')
cidade_splitada = cidade.split()
if (cidade_splitada[0].upper().find('SANTO') == 0):
    resposta = "Sim"
else:
    resposta = "Não"
print('Sua cidade começa com a palavra "santo"? {}'.format(resposta))