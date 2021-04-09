#Desafio 105 - Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: - Quantidade de notas; - A maior nota; - A menor nota; - A média da turma; - A situação (opcional). Adicione também as docstrings da função.
def notas(* valores, sit=False):
    """
    Recebe valores, cria um dicionário adicionando a quantidade de notas, menor nota, maior nota, média de notas e, opcional, a situação da sala.
    :param valores: Notas dos alunos.
    :param sit: Se True, mostra a situação de notas da sala.
    :return: o print do dicionário "retorno"
    """
    bancoDeNotas = list()
    retorno = dict()
    maior = 0
    menor = 0
    media = 0
    somaDeNotas = 0

    for nota in valores:
        somaDeNotas += nota
        bancoDeNotas.append(nota)
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota

    total = len(bancoDeNotas)
    media = somaDeNotas/total

    retorno['total'] = total
    retorno['maior'] = maior
    retorno['menor'] = menor
    retorno['média'] = media
    if sit==True:
        if media >= 7:
            retorno['situação'] = 'BOA'
        elif media < 7 and media > 4:
            retorno['situação'] = 'RAZOÁVEL'
        else:
            retorno['situação'] = 'RUIM'

    return print(retorno)

resp = notas(3,9,9,5,9,9, sit=True)
help(notas)