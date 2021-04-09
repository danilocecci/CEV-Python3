# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a /b
#     print(f'O resultado da divisão entre {a} e {b} é {r}!')
# except:
#     print(f'Deu ruim!')

# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a /b
# except:
#     print(f'Deu ruim!')
# else:
#     print(f'O resultado da divisão entre {a} e {b} é {r}!')

# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a /b
# except Exception as err:
#     print(f'Deu ruim! {err.__class__}')
# else:
#     print(f'O resultado da divisão entre {a} e {b} é {r}!')
# finally:
#     print(f'Foi divertido! Obrigado :D')

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a /b
except (ValueError, TypeError):
    print(f'Deu ruim! Você digitou um valor incorreto!')
except ZeroDivisionError:
    print(f'Deu ruim! Você atribuiu valor "0" ao denominador! Não é possível dividir o {a} pelo {b}.')
except KeyboardInterrupt:
    print(f'Deu ruim! Você quis parar com a brincadeira!')
else:
    print(f'O resultado da divisão entre {a} e {b} é {r}!')
finally:
    print(f'Foi divertido! Obrigado :D')