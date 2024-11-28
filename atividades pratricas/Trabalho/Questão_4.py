
def opcao1():
    global contatos
    print('-'*45)
    print('-'*10, 'MENU CADRASTRO CONTATO','-'*10)
    id = int(input('ID do contato: '))
    nomePessoa = input('Entre com o nome do usuario: ')
    atividade = input ('Entre com a profissão')
    telefone = int(input('Digite o numero de telefone DD 9XXXX-XXXX'))
 

def ValidaopcaoMenu():
    while True:
        try:
            pergunta = (input('>>'))
            if pergunta == '1':
                pergunta = opcao1()
            
            elif pergunta == '2':
                print('Opção indiponivel')

            elif pergunta == '2':
                print('Opção indiponivel')

            elif pergunta == '3':
                print('Opção indiponivel')
            
            elif pergunta == '4':
                print('Encerrando o programa...')
                break 
            else:
                print('Opção invalida. Digite a opção valida (1/2/3/4)')
        except ValueError:
            print('Opção não valida. Digite uma nova opção')

#Tela inical
print('Bem vindo a lista de contados do Robson Carolino')
print('-'*50)
print('-'*17, 'MENU PRINCIPAL', '-'*17)
print('Escolha um das opções desejadas:')
print('1 - Cadrastar contado')
print('2 - Consultar contado(s)')
print('3 - Remover contado')
print('4 - Sair')
opcaoMenu = ValidaopcaoMenu()


listaContatos = []




"""#Tela de boas vindas 

print('Bem vindos a lista de contatos do Robson Carolino') 

print('-'*60) 

print('-'*22,'MENU PRINCIPAL','-'*24) 

# Lista para armazenar os contatos 

lista_contatos = [] 

# ID global inicializado com o número do RU 

id_global = 5000406 


#Tela de Cadrastro 
def cadastrar_contato(id): 

    print('-'*60) 

    print('-'*17, 'MENU CADASTRAR CONTATOS', '-'*18) 

    idContato = input('Id do contato: ') 

    nome = input('Por favor entre com o nome do contato: ') 

    atividade = input('Por favor entre com a atividade do contato: ') 

    telefone = input('Por favor entre com o telefone do contato: ') 

     

    #Cria um dicionário para o contato 

    contato = { 

        'id': id, 

        'nome': nome, 

        'atividade': atividade, 

        'telefone': telefone 

    } 

    #Adiciona o contato à lista de contatos 

    lista_contatos.append(contato.copy()) 

     
#Mensagem de sucesso 
    print('Contato criado!') 

 
#variaval para consultar
def consultar_contatos(): 

    print('-'*60) 

    print('-'*17,'MENU CONSULTAR CONTATOS','-'*20) 

    while True: 

        opcao = int(input('Escolha a opção deseja: \n1 - Consultar Todos os Contatos \n2 - Consultar Contato por Id \n3 - Consultar Contatos(s) por Atividade \n4 - Retornar \n>> ')) 

         

        if opcao == 1: 

            if not lista_contatos:  #verifica se a lista está vazia 

                print('Nenhum contato cadastrado.') 

            else: 

                for contato in lista_contatos: 

                    print(f'ID: {contato['id']}') 

                    print(f'Nome: {contato['nome']}') 

                    print(f'Atividade: {contato['atividade']}') 

                    print(f'Telefone: {contato['telefone']}') 

                    print()  

                    print('-' * 20) 

        elif opcao == 2: 

            #consulta por ID 

            id_consulta = int(input('Informe o ID do contato: ')) 

            for contato in lista_contatos: 

                if contato['id'] == id_consulta: 

                    print(f'ID: {contato['id']}') 

                    print(f'Nome: {contato['nome']}') 

                    print(f'Atividade: {contato['atividade']}') 

                    print(f'Telefone: {contato['telefone']}') 

                    print()  

                    print('-' * 20) 

                    break 

            else: 

                print('Contato não encontrado.') 

        elif opcao == 3: 

            #consulta por Atividade 

            atividade_consulta = input('Informe a atividade: ') 

            for contato in lista_contatos: 

                if contato['atividade'].lower() == atividade_consulta.lower(): 

                    print(f'ID: {contato['id']}') 

                    print(f'Nome: {contato['nome']}') 

                    print(f'Atividade: {contato['atividade']}') 

                    print(f'Telefone: {contato['telefone']}') 

                    print()  

                    print('-' * 20) 

        elif opcao == 4: 

            # Retornar ao menu principal 

            return 

        else: 

            print('Opcao inválida') 

 
#varialvel para remover contato 
def remover_contato(): 

    print('-'*60) 

    print('-'*18,'MENU REMOVER CONTATOS','-'*21) 

    while True: 

        id_remover = int(input('Digite o ID do contato a ser removido: ')) 

        for contato in lista_contatos: 

            if contato['id'] == id_remover: 

                lista_contatos.remove(contato) 

                print('Contato removido com sucesso!') 

                return 

        print('ID inválido') 

 

# Estrutura principal do menu 

while True: 

    opcao_menu = int(input('Escolha a opcao desejada: \n1 - Cadastrar Contato  \n2 - Consultar Contato(s)  \n3 - Remover Contato  \n4 - Sair \n>>')) 

    if opcao_menu == 1: 

        id_global += 1 

        cadastrar_contato(id_global) 

    elif opcao_menu == 2: 

        consultar_contatos() 

    elif opcao_menu == 3: 

        remover_contato() 

    elif opcao_menu == 4: 

        print('Programa encerrado.') 

        break 

    else: 

       print('Opcao inválida') """
