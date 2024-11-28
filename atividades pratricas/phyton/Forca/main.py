
import jogo as j
import fileHadley as fh

def mostrar_menu():
    print('='*30)
    print(' '*7 + 'jOGO DA FORCA')
    print('='*30)
    print('\n1 - JOGAR')
    print('2 - SCORE')
    print('3 - Sair\n')
    print('='*30)

arquivo = 'score.txt'
if fh.existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('ARQUIVO NÃO EXISTE.')
    fh.criarArquivo(arquivo)

#Menu
while True:
    mostrar_menu()
    opcao = int(input('Escolha uma opção (1/2/3:) '))

    match (opcao):
        case 1: 
            print('Inicar jogo!')
            j.jogar()

        case 2:
            print('SCORE')
            
        case 3:
            print('Saindo do jogo. Até mais!')
            break    
        case _:
            print('Opção Ivalida. Tente novamente outra opção')