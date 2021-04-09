import colorama
colorama.init()

print('-='*10)
print('\033[1;31mEmpréstimo Bancário\033[m')
print('-='*10)

valor_casa = float(input('Digite o valor do imóvel: '))
salario = float(input('Digite seu salário: '))
prestacao_anual = int(input('Em quantos anos deseja pagar o valor total do imóvel? '))
prestacao_mensal = valor_casa/(prestacao_anual*12)

if prestacao_mensal > salario*0.3:
    print('Sinto muito, mas o empréstimo não poderá ser efetuado. A prestação mensal({} meses) de R${:.2f} superará os 30% do seu salário. :('.format(prestacao_anual*12,prestacao_mensal))
else:
    print('Parabéns. Seu empréstimo foi aprovado!')
