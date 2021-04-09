words = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for word in words:
    print(f'Na palavra {word} temos',end=' ')
    for letter in word:
        if letter.lower() in 'aeiou':
            print(letter.lower(), end=' ')
    print('')