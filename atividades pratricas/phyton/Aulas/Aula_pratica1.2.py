
preco  = float(input('Digite o preço do produto: '))
percentual = float(input('Digite o percentual de desconto (0-100%): '))

desconto = preco * (percentual / 100)
final =  preco - desconto
print(f'o preço do produto é {preco}, o desconto de {percentual}%')
print(f'Valor Calcualdo do desconto: {desconto}, valor final do produto: {final}')