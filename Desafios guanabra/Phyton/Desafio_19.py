#Nome alatoiro para ser escolhido 
import random

n1 = input('Digite o nome do aluno: ')
n2 = input('Digite o nome do aluno: ')
n3 = input('Digite o nome do aluno: ')
n4 = input('Digite o nome do aluno: ')
lista = [n1, n2, n3, n4]

#choice usado para randomizar os nomes

nomeAlatorio = random.choice(lista)

print(f'O aluno selecuinado foi {nomeAlatorio}')