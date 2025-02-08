
print('Lanchonete')
print('1-Coxinha R$ 5,00')
print('2-Pastel R$ 7,00')
print('3-Café R$ 4,00')
print('4-Suco R$ 6,00')
print('5-Sair')

total = 0
while True:
    op = int(input('Qual item gostaria de comprar? '))

    if op == 1:
        qtd = int(input('Quantas unidades gostaria de comprar? '))
        total += qtd * 5

    elif op == 2:
        qtd = int(input('Quantas unidades gostaria de comprar? '))
        total += qtd * 7

    elif op == 3:
        qtd = int(input('Quantas unidades gostaria de comprar? '))
        total += qtd * 4

    elif op == 4:
        qtd = int(input('Quantas unidades gostaria de comprar? '))
        total += qtd * 6

    elif op == 5:
        break

    else:
        print('Produto inválido, selecione outro.')

print(f'O total a ser pago é de R$ {total}.')