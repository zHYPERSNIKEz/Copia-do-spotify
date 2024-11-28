#Caucular area 

altura = float(input('Digite o valor da altura em metros: '))
largura = float(input('Digite o valor da largura em metros: '))

area = altura * largura 
tinta = 2 

resultado = area // tinta

print(f'A quantidade de tinta é de {resultado:.0f}')