import os


#Força o usuario a escolher uma opção
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x >max)):
        x = int(input(pergunta))
    return x 

#Abrir e fechamento do arquivo
def existeAquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'at')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
#Criar arquivo 
def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Falha na criação do arquivo')
    else:
        print(f'Arquivo {nomeArquivo}criado com sucesso\n')
        return True

#Cadastar Jogo
def cadastarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'a')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write(f'{nomeJogo};{nomeVideogame}\n')
    finally:
        a.close()

#Listar arquivo 
def listarAquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler arquivo.')
    else:
        print(a.read())

    finally:
        a.close()

#programa principal 
arquivo = 'games.txt'
if existeAquivo (arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente')
    criarArquivo(arquivo)
while True:
    print('Menu')
    print('1 - Cadrastar novo item')
    print('2 - Lista de cadtastro')
    print('3 - Sair')

    op = valida_int('Escolha a opção desejada: ',1, 3)
    if ( op == 1): #Novo item
        print ('Opção de cadrastar novo item seleciado...\n')
        nomeJogo = input('Digite o nome do jogo: ')
        nomeVideogame = input('Digite o nome do videogame: ')
        cadastarJogo (arquivo, nomeJogo, nomeVideogame)
    
    elif (op == 2): #Lista de item 
        print ('Opção de lista de item seleciado...\n')
        listarAquivo(arquivo)
    
    elif (op == 3): #Sair
        print('Encerranndo o programa...')
        break
