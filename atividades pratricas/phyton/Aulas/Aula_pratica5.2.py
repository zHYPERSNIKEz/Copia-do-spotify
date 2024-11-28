#jogo pedra papel tesoura 

import random

#obrigar a pessoas a escolher uma opção
def valida_int(pergunta, min, max):
        x = int(input(pergunta))
        while (x < min or x > max):
            x = int(input(pergunta))
        return x 

         

#sistema de vitorias
def vencedor (jogador1, jogador2):
    global v1, v2, empate
    if jogador1 == 1: #pedra inicio
        if jogador2 == 1: #pedra
            empate += 1
        elif jogador2 == 2: #Papel 
            v2 += 1
        elif jogador2 == 3: #tesoura
            v1 += 1

    elif jogador1 == 2: #papel inico 

        if jogador2 == 1: #pedra
            v1 += 1
        elif jogador2 == 2: #Papel 
            empate += 1
        elif jogador2 == 3: #tesoura
            v2 += 1

    elif jogador1 == 3: #Tesoura inicio
        if jogador2 == 1: #pedra
            v2 += 1
        elif jogador2 == 2: #Papel 
            v1 += 1
        elif jogador2 == 3: #tesoura
            empate += 1

    resultados = [v1, v2, empate]
    return resultados

#tela inicial

print('-------JOKENPO-------')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
print('0 - Sair')

jogadas = []
resultados = []
v1 = 0
v2 = 0
empate = 0

while True:
    j1 = valida_int('Escolha sua jodada: ', 0, 3)
    if not j1:
        break
    j2 = random.randint(1,3)
    jogadas.append([j1, j2])
    resultados = vencedor(j1, j2)

for jogada in jogadas: 
    for dado in jogada:
        print(dado, end = ' ')
    print()

print(f'Número de vitorias do jogador 1: {resultados[0]}')
print(f'Número de vitorias do jogador 2: {resultados[1]}')
print(f'Número de empates: {resultados[2]}')

