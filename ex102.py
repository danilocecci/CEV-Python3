#Desafio 102 - Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def factorial(number, show=False):
    """
    Realiza o fatorial de um número, se por passado o parâmetro 'True', será mostrado a conta.
    :param number: Número usado para calcular a fatorial.
    :param show: Se True, mostra a conta.
    :return: sem retorno
    """
    factor = 1
    for counter in range(number, 0, -1):
        factor *= counter
        if show == True:
            if counter == 1:
                print(f'{counter} = ', end='')
            else:
                print(f'{counter} x ', end='')
    print(factor)

factorial(5, True)
# help(factorial)