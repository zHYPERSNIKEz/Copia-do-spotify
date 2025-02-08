#mostar angulos de um grau escolhido pelo usuario 
import math

anguloGrau = float(input('Digite o angulo em gruas: '))

# Converte o ângulo para radianos
anguloRadiante = math.radians(anguloGrau)

seno = math.sin(anguloRadiante)
cosseno = math.cos(anguloRadiante)
tangente = math.tan(anguloRadiante)

print(f'O seno de {anguloGrau} é {seno:.2f}')
print(f'O seno de {anguloGrau} é {cosseno:.2f}')
print(f'O seno de {anguloGrau} é {tangente:.2f}')