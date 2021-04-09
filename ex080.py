num = list()
for c in range(0,5):
    handle_num = int(input('Digite um número inteiro: '))
    if c == 0 or handle_num > num[-1]:
        num.append(handle_num)
    else:
        count = 0
        while count < len(num):
            if handle_num <= num[count]:
                num.insert(count, handle_num)
                break
            count += 1
print('')
print(f'Os valores informados em ordem crescente foram: {num}')