import datetime

person = dict()

person['name'] = str(input('Nome: '))
year = int(input('Ano de Nascimento: '))
person['age'] = datetime.date.today().year - year
person['jobBook'] = int(input('Carteira de trabalho: '))
if person['jobBook'] != 0:
    person['contract'] = int(input('Ano de Contratação: '))
    person['retire'] = person['age'] + ((person['contract']+35) - datetime.date.today().year)
    person['salary'] = int(input('Salário: ')) 

print('-='*10+'-')
if person['jobBook'] != 0:
    print(f"Olá, {person['name']}! Espero que esteja tudo bem! :D\nVocê tem {person['age']} anos de idade.\nSua carteira de trabalho é '{person['jobBook']}'.\nFoi contratado(a) no ano de {person['contract']}.\nCom salário de R${person['salary']}.\nIrá se aposentar com {person['retire']} anos de idade!")
else:
    print(f"Olá, {person['name']}! Espero que esteja tudo bem! :D\nVocê tem {person['age']} anos de idade.\nNo momento, você não está trabalhando!\nSem problemas. Jájá você consegue o trabalho que sempre sonhou! Boa sorte :D")
