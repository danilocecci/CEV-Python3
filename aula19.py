# pessoas = {
#     'nome': 'Gustavo',
#     'sexo': 'M',
#     'idade': 22
# }
#print(pessoas)

#print(f"O {pessoas['nome']} tem {pessoas['idade']} anos e é do sexo {pessoas['sexo']}")

# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())
#pessoas['nome'] = 'João'

# pessoas['peso'] = 98.5

# for k, v in pessoas.items():
#     print(f'{k} = {v}')

# brasil = list()

# estado1 = {
#     'uf':'Rio de Janeiro',
#     'sigla': 'RJ'
#     }

# estado2 = {
#     'uf':'São Paulo',
#     'sigla': 'SP'
#     }

# brasil.append(estado1)
# brasil.append(estado2)

# print(estado1)
# print(estado2)
# print(brasil)
#print(brasil[0]['uf'])
#print(brasil[1]['sigla'])

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for v in e.values():
        print(f'{v}',end=' ')
    print()