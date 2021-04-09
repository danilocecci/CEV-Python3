def getMaxNum(* num):
    maxNum = 0
    counter = 0

    while True:
        num = int(input('(Para sair, digite a senha "9156")\nInsira um número: '))
        if num == 9156:
            break
        elif num > maxNum:
            maxNum = num
            counter += 1
        else:
            counter += 1

    print(f'Você me informou {counter} números. O maior número informado foi "{maxNum}"!')
getMaxNum()