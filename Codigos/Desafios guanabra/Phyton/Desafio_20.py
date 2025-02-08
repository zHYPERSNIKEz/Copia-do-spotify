#lista aleatoaria

import random

n1 = input('Digite o primeiro nome:')
n2 = input('Digite o segundo nome:')
n3 = input('Digite o terceiro nome:')
n4 = input('Digite o quarto nome:')

lista = [n1, n2, n3, n4]
 #shuffle usado para lista aleatoria
random.shuffle(lista)

print(f'A ordem de apresentação é {lista}')