student = dict()

student['Nome'] = str(input('Nome do aluno: '))
student['Média'] = float(input(f'Média de {student["Nome"]}: '))
if student['Média'] <= 6:
    student['Situação'] = 'Reprovado'
else:
    student['Situação'] = 'Aprovado'

print('-='*20+'-')
for k, v in student.items():
    print(f'{k} é igual a {v}!')