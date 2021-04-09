from random import randint

handle_tuple = []

for c in range(0,5):
    handle_tuple.append(randint(0,99))

sorted_tuple = sorted(handle_tuple)

print(f'Foi gerado essa tupla => {handle_tuple}')
print(f'O menor número da tupla é {sorted_tuple[0]}!\nO maior número da tupla é {sorted_tuple[-1]}!')