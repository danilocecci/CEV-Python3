n1 = int(input('Digite qualquer número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = int(input('Digite mais um número inteiro: '))

if n1 > n2:
    if n1 > n3:
        print('{} é o maior número e o {} é o menor'.format(n1,n2))
    else:
        print('{} é o maior número e o {} é o menor'.format(n3,n2))
else:
    if n2 > n3:
        print('{} é o maior número e o {} é o menor'.format(n2,n3))
    else:
        print('{} é o maior número e o {} é o menor'.format(n3,n1))