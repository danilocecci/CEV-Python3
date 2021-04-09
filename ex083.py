expression = str(input('Digite uma expressão que contenha parênteses: '))
parenthesis_counter = 0

for char in expression:
    if char == '(':
        parenthesis_counter += 1
    elif char == ')':
        parenthesis_counter -= 1
        if parenthesis_counter < 0:
            break

if parenthesis_counter == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')