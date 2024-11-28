#Calcular hipotenusa
from math import hypot

catetoOposto = float(input('Digite o valor do cateto oposto:'))
catetoAdjacento = float(input('Digite o valor do cateto adjacento:'))

hipotenusa = hypot(catetoOposto, catetoAdjacento)

print(f'A hipotenusa é {hipotenusa}')