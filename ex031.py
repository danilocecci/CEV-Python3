distancy = int(input('Digite a distância percorrida (em Km) por sua viagem: '))
if distancy > 200:
    price = distancy*0.45
    print('Sua viagem de {}Km ficou em R${:.2f}!'.format(distancy,price))
else:
    price = distancy*0.5
    print('Sua viagem de {}Km ficou em R${:.2f}!'.format(distancy,price))
