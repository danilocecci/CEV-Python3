analyze = input('Digite algo para ser analizado: ')
print('')
print('Analizando...')
print('')
if (analyze.isalnum() == True):
    print('"{}" é Alfanumérico!'.format(analyze))
    if (analyze.isnumeric() == True):
        if (analyze.isdecimal() == True):
            print('"{}" é um número Decimal!'.format(analyze))
        elif (analyze.isdigit() == True):
           print('"{}" é um Dígito!'.format(analyze))
        else:
            print('"{}" não é um Dígito!'.format(analyze))
    else:
        print('"{}" não é composto apenas por números!'.format(analyze))
    if (analyze.isalpha() == True):
        if (analyze.islower() == True):
            print('"{}" é composto apenas por letras minúsculas!'.format(analyze))
        elif (analyze.isupper() == True):
            print('"{}" é composto apenas por letras maísculas!'.format(analyze))
        else:
            print('"{}" é composto por letras maísculas e minúsculas'.format(analyze))
    else:
        print('"{}" não é formado apenas por letras!'.format(analyze))
else:
    print('Poxa... você não digitou nada. "Enter" não vale! :(')

