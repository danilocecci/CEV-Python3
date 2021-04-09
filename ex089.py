gradebook = [[],[[],[]],[]]
keep = 's'
counter = 0
handle_average = 0
student = 0

while keep == 's':
    gradebook[0].append(str(input('Nome: ')))
    gradebook[1][0].append(float(input('Nota1: ')))
    gradebook[1][1].append(float(input('Nota2: ')))
    handle_average = gradebook[1][0][counter] + gradebook[1][1][counter]
    gradebook[2].append(handle_average/2)
    keep = str(input('Deseja continuar? [S/N] R: ')).lower()
    counter += 1
print('')
print('-='*10+'-')
print('  ID   NOME   MÉDIA')
for c in range(0,len(gradebook[0])):
    print(f'{c:^5} {gradebook[0][c]:^5} {gradebook[2][c]:^6}')

while student != 999:
    print('-='*10+'-')
    student = int(input('Digite o ID do aluno para saber suas notas!\nSe digitar um ID inexistente ou 999, o programa encerrará!\nID: '))
    if student > len(gradebook[0]):
        break
    print(f'Você escolheu o aluno "{gradebook[0][student]}".\nSuas notas: {gradebook[1][0][student]} e {gradebook[1][1][student]}\nSua média final: {gradebook[2][student]}')

print('Obrigado!')