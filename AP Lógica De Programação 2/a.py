lista_livro = []
id_global = 0

def boas_vindas():
    # Mensagem de boas-vindas
    print('Bem vindo a livraria do Issac') 

def cadastrar_livro(id):
    nome = input('Digite o nome do livro: ') # Pergunta o nome do livro
    autor = input('Digite o nome do autor: ') # Pergunta o nome do autor
    editora = input('Digite p nome da editora: ') # Pergunta o nome da editora 

    lista_dicionario = {'id':id,
                        'nome':nome,
                        'autor':autor,
                        'editora':editora}

    lista_livro.append(lista_dicionario)
    id_global += 1

def consultar_livro():
    opcoes = ''
    while not opcoes:
        print('Qual opção deseja?')
        print('1. Consultar todos')
        print('2. Consultar por ID')
        print('3. Consultar por Autor')
        print('4. Retornar ao menu')
        opcoes = input('>> ')

        if opcoes in ('1','2','3'):
            continue
        else:
            print('Retornando ao menu principal...')
            return

def remover_livro():
    id_remover = int(input('Digite o ID do livro a ser removido: '))

    for livro in lista_livro:
        if livro['id'] == id_remover:
            lista_livro.remove(livro)
            break
    else:
        print('ID inválido. Livro não encontrado...')

def menu_principal():
    boas_vindas()
    while True:
        print('Escolha a opção desejada')
        print('1 - Cadastrar livro')
        print('2 - Consultar livro(s)')
        print('3 - Remover livro')
        print('4 - Sair')
        opcao_menu = input('>> ')

        if opcao_menu == '1':
            cadastrar_livro(id=1)

        elif opcao_menu == '2':
            consultar_livro()

        elif opcao_menu == '3':
            remover_livro()

        else:
            print('Fechando o programa...')
            break


menu_principal()