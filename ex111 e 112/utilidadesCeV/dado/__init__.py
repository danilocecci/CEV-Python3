def leiaDinheiro(texto):
    validaInput = False
    while validaInput == False:
        inputValue = str(input(texto)).replace(",",".").replace(" ","")
        if inputValue.isalpha():
            print(f'ERRO: "{inputValue}" não é um preço válido!')
        else:
            return float(inputValue)