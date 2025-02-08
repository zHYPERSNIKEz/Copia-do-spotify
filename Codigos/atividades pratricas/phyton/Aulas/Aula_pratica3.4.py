total = 0
dinheiro = 0
acc_idade = 0

while True:
    idade = int(input('Digite sua idade:'))
    print('Digite 0 para encerrar o programa')
    if idade == 0:
        break
    
    total += 1
    acc_idade += idade
    if idade < 3:
        ingresso = 0 
    else:
        if idade >= 12:
            ingresso = 30
        else:
            ingresso = 15
    dinheiro += ingresso

if total == 0:
    print('Digite uma idade valida')
else:
    media = acc_idade // total

    print(f'Total de pessoas: {total}')
    print(f'Total arrecado: {dinheiro}')
    print(f'Media de idades: {media:.2f}')

