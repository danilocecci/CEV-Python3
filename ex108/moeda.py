#Referente ao desafio 108 - Ver em ex108.py
def aumentar(numero=0, porcentagem=0):
    resultuado = numero*(1 + porcentagem/100)
    return resultuado

def diminuir(numero=0, porcentagem=0):
    resultado = numero*(1 - porcentagem/100)
    return resultado

def dobro(numero=0):
    resultado = numero*2
    return resultado

def metade(numero=0):
    resultado = numero/2
    return resultado

def moeda(numero=0, moeda='R$'):
    return f'{moeda}{numero:>.2f}'.replace('.',',')