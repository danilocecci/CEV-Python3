sequence = int(input('Digite a quantidade de números fibonacci que deseja: '))
numbers = [0, 1]
counter = 2

while counter < sequence:
    numbers.append(numbers[counter-1]+numbers[counter-2])
    counter += 1

print(numbers)