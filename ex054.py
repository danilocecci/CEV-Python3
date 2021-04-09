from datetime import datetime
import colorama
colorama.init()

print('-='*5+'-')
print('\033[1;31mMAIORIDADE\033[m')
print('-='*5+'-')

print('Vamos descobrir quantas pessoas já atigiram a maioridade!')
ano_nascimento = []
agora = datetime.now()

maioridade = 0

for c in range(1,8):
    ano_nascimento = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = agora.year - ano_nascimento
    if idade >= 21:
        maioridade += 1

if maioridade == 0:
    print('Nenhuma dessas pessoas atigiu a maioridade!')
elif maioridade > 0 and maioridade < 4:
    print('Apenas {} pessoa(s) atingiu(ram) a maioridade!'.format(maioridade))
    print('As outras {} pessoas não atingiram a maioridade!'.format(7-maioridade))
elif maioridade > 4 and maioridade < 7:
    print('{} pessoas atingiram a maioridade!'.format(maioridade))
    print('As outras {} pessoas não atingiram a maioridade!'.format(7-maioridade))
else:
    print('Todas as pessoas atingiram a maioridade!')