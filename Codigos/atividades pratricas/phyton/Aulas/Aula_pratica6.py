#uso da case no lugar do if e elif
print('Escolha produto')
print('1 - maça')
print('2 - laranja')
print('3 - banana')
produto = int(input('Qual a sua escolha?'))
qtd = int(input('Quantas unidades? '))

match (produto):
        case 1 :
                pagar = qtd *2.3
                print(f'Você comprou {qtd} maças. total a pagar: {pagar}')
        case 2:
                pagar = qtd * 3.6
                print(f'Você comprou {qtd} laranja. total a pagar: {pagar}')
                
        
        case 3:
                pagar = qtd *1.85
                print(f'Você comprou {qtd} banasa. total a pagar: {pagar}')
        
        case _:

                print('Produto inexistente!')




#uso da case para checagem de tipo de dado que é

def checagem_tipo(dado):
        match dado:
                case str(dado):
                        print('String:', dado)
                case int(dado):
                        print('Inteiro:', dado)
                case float(dado):
                        print('Float', dado)
                case _:
                        print('Tipo desconhecido de dado')
dados = ['Phyton', 42, 3.14, 23, 'C']

for dado in dados:
        checagem_tipo(dado)
