import colorama, time
colorama.init()

print('-='*10+'-')
print('\033[1;31mCATEGORIA DE NATAÇÃO\033[m')
print('-='*10+'-')

year = int(input('Digite o ano que você nasceu: '))
years_old = int(time.strftime("%Y"))-year
print('Você tem {} anos!'.format(years_old))

if years_old <= 9:
    print('Sua categoria é: \033[1mMIRIM\033[m!')
elif years_old >= 10 and years_old <= 14:
    print('Sua categoria é: \033[1mINFANTIL\033[m!')
elif years_old >= 15 and years_old <= 19:
    print('Sua categoria é: \033[1mJUNIOR\033[m!')
elif years_old == 20:
    print('Sua categoria é: \033[1mSENIOR\033[m!')
else:
    print('Sua categoria é: \033[1mMASTER\033[m!')