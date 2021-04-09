#Referente ao desafio 108 - Ver em ex108.py
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