#conta quantos no numero espercifico aparece 

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
#count serve para escolher a nota 
print(notas)
print(f'O resultado de numeros 7 é: {notas.count(7)}' )

#altera a ultima nota para 4

notas[-1] = 4

print(f'{notas}')

#encontra a maior nota

print(f'A maior nota é {max(notas) }')

#ordernar notas 
notas.sort()
print(f'a notas ordenada\n{notas}')

#media das notas

print(f'a media das notas é:\n {sum(notas) / len(notas)}')
