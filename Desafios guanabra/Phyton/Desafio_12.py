#Ler um valor e disser que quando ele custa com 5% de desconto 

valor = float(input('Digite o valor: '))

desconto = 0.5 # desconto de 5%

resultado = valor - desconto

print(f'O valor do produto é {valor:.0f} e com o desconto de 5% fica {resultado:.1f}')