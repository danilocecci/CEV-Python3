nome = input('Digite seu nome completo: ')
nome_splitado = nome.lower().split()
tem_silva = False
for i in range(len(nome_splitado)):
    if (nome_splitado[i] == "silva"):
        tem_silva = True
        break
    i = i + 1

if (tem_silva == True) :
    print('Que legal, você tem "Silva" em seu nome!')
else:
    print('Verifiquei e você não tem "Silva" em seu nome! Era só curiosidade mesmo :SMILES:')
