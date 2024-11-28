#Ver se ano é bissexto
ano = int(input('Digite o ano: '))

if (ano % 4 == 0):
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')

#Se ambas variaveis forem verdadeiras

cima = True
baixo = True

if(cima == True or baixo == True):
    print('Escolha um caminho')
else:
    print('Você escolheu um caminho')