#Criar um programa que leia o numero e mostre o dobro, triplo e raiz quadrada 
import math 
numero = int(input('Digite o numero: '))

dobro = numero * 2 
triplo = numero * 3
raiz = math.sqrt (numero)

print(f'A o dobro de {numero} é: {dobro} \n o triplo é: {triplo} \n a raiz quadrada é: {raiz:.3f}')