kwh = float(input('Quantos Kwh foram usados?'))
tipo = input('Qual o tipo de intalação? Digite R(Residencial), C(Comecial) ou I(Industrial)' )

if (tipo == "R"):
    if (kwh >= 500):
        preco = 0.65
    else:
        preco = 0.4
    print(f'valor a pagar é: {kwh * preco}')
elif (tipo == "C"):
    if (kwh >= 1000):
        preco = 0.6
    else:
        preco = 0.55
    print(f'valor a pagar é: {kwh * preco}')
elif (tipo == "I"):
    if (kwh >= 5000):
        preco = 0.6
    else:
        preco = 0.55
    print(f'valor a pagar é: {kwh * preco}')
else:
    print('Intalação invalida. Encerrando...')