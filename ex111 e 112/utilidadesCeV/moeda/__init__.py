#Referente ao desafio 110 - Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
def aumentar(numero=0, porcentagem=0, format=False):
    resultado = numero*(1 + porcentagem/100)
    return resultado if not format else moeda(resultado)

def diminuir(numero=0, porcentagem=0, format=False):
    resultado = numero*(1 - porcentagem/100)
    return resultado if not format else moeda(resultado)

def dobro(numero=0, format=False):
    resultado = numero*2
    return resultado if not format else moeda(resultado)

def metade(numero=0, format=False):
    resultado = numero/2
    return resultado if not format else moeda(resultado)

def moeda(numero=0, moeda='R$'):
    return f'{moeda}{numero:>.2f}'.replace('.',',')

def resumo(preço=0, aumento=20, reducao=80):
    print('-='*15+'-')
    print('Resumo'.center(30))
    print('-'*31)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, format=True)}')
    print(f'Metade do preço: \t{metade(preço, format=True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preço, aumento, format=True)}')
    print(f'{reducao}% de redução: \t{diminuir(preço, reducao, format=True)}')
    print('-='*15+'-')