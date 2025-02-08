#escrever um algoritimo que criaruma tupla com 10 palavras e enconta dentro dela as vogais e imprime cada palavra da vogal correspondida 

palavras = ('Mario', 'Luigi', 'Peach', 'Yoshi', 'Bowser')

for palavra in palavras:
    print(f'\nPalavras: {palavra.upper()}, Vogais:', end= ' ')
    for letra in palavra:
       if letra.lower() in 'aeiou': 
           print(letra.upper(), end = ' ')


