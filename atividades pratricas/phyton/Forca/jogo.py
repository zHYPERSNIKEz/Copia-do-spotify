import desenhos as d
import fileHadley as fh
from random import choice


def jogar():

    lista_palavras = list()
    arquivo = fh.abrirArquivoLeitura('palavras.txt')
    for linha in arquivo:
        palavra = linha.strip()
        lista_palavras.append(palavra)

    palavra_sorteada = choice (lista_palavras) # type: ignore

#organizar a tela para sumir as palavras de inicio
    for x in range(50):
        print()

    digitadas = []
    acertos = []
    erros = 0 

    #Inico do programa 
    nome = input('Quem está jogado? ')

    while True:
        advinha = d.imprimir_palavras_secreta(palavra_sorteada, acertos)
        
        #CONDIÇÃO  DE VITORIA
        if advinha == palavra_sorteada:
            print('Você ganho o jogo!')
            break

        #TENTATIVAS
        tentativas  = input('\nDigite uma letra: ').lower().strip()
        if tentativas in digitadas:
            print('Você já usou e essa letra!')
            continue
        else:
            digitadas += tentativas #ou append
            if tentativas in palavra_sorteada:
                acertos += tentativas
            else:
                erros += 1
                print ('Você erro!')

        score = d. desenhar_forca(erros)

    #CONDIÇÃO DE FIM  DE JOGO
        if erros == 6:
            print('Enforcado!')
            print(f'A palavra correta era { palavra_sorteada}.')
            break
        fh.inserir_score('score.txt', nome, score)