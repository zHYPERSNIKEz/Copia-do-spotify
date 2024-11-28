#Locadora de carro

carro = 60
km = 0.6

print('Bem vindo a locadora de carros')

dias = int(input('Digite a quantidade de dias: '))
kmRodados = float(input('Quantos kms rodados: '))

valorAluguel = carro * dias 
kmValor = km * kmRodados

valorFinla = valorAluguel + kmValor

print(f'Você alugou o carro por {dias} dias e roudou por {kmRodados} km, o valor final foi de {valorFinla:.2f}')
