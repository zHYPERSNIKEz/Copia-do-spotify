print('Cauculadora')
print('+ adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Precione qualquer outra tecla para sair')

op = input('Qual oporeação deseja realiza?')
x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor'))

if ( op == '+'):
    res = x + y 
    print(f'o resultodo de {x} + {y} é: {res}')
elif ( op == '-'):
    res = x - y 
    print(f'o resultodo de {x} - {y} é: {res}')
elif ( op == '*'):
    res = x * y 
    print(f'o resultodo de {x} * {y} é: {res}')
elif ( op == '/'):
    res = x / y 
    print(f'o resultodo de {x} / {y} é: {res}')
else:
    print('Encerramos o programa...')