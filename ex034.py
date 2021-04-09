print('Hoje é dia de aumentooo!!')
salary = float(input('Digite seu salário: R$'))
if salary == 1250:
    salary = salary*1.5
    print('Já que seu salário é exatamente R$1.250,00, seu aumento foi de 15% totalizando R${:.2f}!'.format(salary))
else: 
    if salary > 1250:
        salary = salary*1.1
        print('Já que seu salário é superior a R$1.250,00, seu aumento foi de 10% totalizando R${:.2f}!'.format(salary))
    else:
        salary = salary*1.5
        print('Já que seu salário é inferior a R$1.250,00, seu aumento foi de 15% totalizando R${:.2f}!'.format(salary))