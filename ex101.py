from datetime import date

def vote(yearsOld):
    if yearsOld < 16:
        return 0
    elif yearsOld >= 16 and yearsOld < 18 or yearsOld > 60:
        return 1
    else:
        return 2


handleAge = int(input('Digite o ano de seu nascimento: '))
yearsOld = date.today().year - handleAge
vote = vote(yearsOld)
if vote == 0:
    print(f'Você ainda não pode votar por ter {yearsOld} anos!')
elif vote == 1:
    print(f'Seu voto é opcional por ter {yearsOld} anos!')
else:
    print(f'Seu voto é obrigatório por ter {yearsOld} anos!')