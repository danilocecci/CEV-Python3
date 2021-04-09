km = float(input('Digite quantos KM foram percorridos: '))
days = int(input('Por quantos dias utilizou o veículo? '))
price = (km*.15) + (60*days)
print('O valor total por utilizar nosso veículo alugado foi de R${}!'.format(price))
