from random import randint
from time import sleep

def sort():
    for c in range(0,5):
        num.append(randint(0,9))
        c += 1
    print(f'Sorteando 5 valores da lista: ', end='')
    for v in num:
        print(f'{v}',end=' ', flush=True)
        sleep(0.5)
    print('Pronto!')

def oddSum():
    counterOdds = 0
    oddSumResult = 0
    for v in num:
        if v % 2 == 0:
            counterOdds += 1
            oddSumResult += v
    print(f'Somando os valores pares de {num}, temos {oddSumResult}!')

num = list()


sort()
oddSum()