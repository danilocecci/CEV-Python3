def escreva(userInput):
    if len(userInput)%2 != 0:
        print('~'*(len(userInput)*2-1))
        print(userInput.center(len(userInput)*2))
        print('~'*(len(userInput)*2-1))
    else:
        print('~'*len(userInput)*2)
        print(userInput.center(len(userInput)*2))
        print('~'*len(userInput)*2)

userInput = str(input('Digite um texto para personalizar: '))
escreva(userInput)