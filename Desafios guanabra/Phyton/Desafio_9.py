#Leia um numero qualquer e mostre a sua tabuada

valor = float(input('Digite o seu numero: '))

for i in range(1, 11):
    print(f'O {valor:.0f} vezes {i} é: {valor*i:.0f}')

