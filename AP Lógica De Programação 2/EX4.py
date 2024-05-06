

# Função para cadastrar um livro na lista de livros
def cadastrar_livro(id):
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    editora = input("Digite o nome da editora: ")

    livro = {"id": id, "nome": nome, "autor": autor, "editora": editora}
    lista_livros.append(livro)
    print("Livro cadastrado com sucesso!")

# Função para consultar livros
def consultar_livro():
    while True:
        print("Opções de consulta:")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Autor")
        print("4. Retornar ao menu")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':  # Consultar Todos
            print("Todos os livros:")
            for livro in lista_livros:
                print(livro)
        elif opcao == '2':  # Consultar por Id
            id_busca = int(input("Digite o Id do livro: "))
            for livro in lista_livros:
                if livro["id"] == id_busca:
                    print("Livro encontrado:")
                    print(livro)
                    break
            else:
                print("Livro não encontrado.")
        elif opcao == '3':  # Consultar por Autor
            autor_busca = input("Digite o nome do autor: ")
            livros_encontrados = [livro for livro in lista_livros if livro["autor"] == autor_busca]
            if livros_encontrados:
                print("Livros do autor encontrados:")
                for livro in livros_encontrados:
                    print(livro)
            else:
                print("Nenhum livro encontrado para esse autor.")
        elif opcao == '4':  # Retornar ao menu
            break
        else:
            print("Opção inválida!")

# Função para remover um livro da lista de livros
def remover_livro():
    id_remover = int(input("Digite o Id do livro a ser removido: "))
    for livro in lista_livros:
        if livro["id"] == id_remover:
            lista_livros.remove(livro)
            print("Livro removido com sucesso!")
            break
    else:
        print("Id inválido. Livro não encontrado.")

# Variáveis globais
lista_livros = []
id_global = 1

def run():
    # Mensagem de boas-vindas
    print("Bem-vindo ao sistema de gerenciamento de livros!")

    # Menu principal
    while True:
        print("\nOpções:")
        print("1. Cadastrar Livro")
        print("2. Consultar Livro")
        print("3. Remover Livro")
        print("4. Encerrar Programa")
        opcao_menu = input("Escolha uma opção: ")

        if opcao_menu == '1':  # Cadastrar Livro
            cadastrar_livro(id_global)
            id_global += 1
        elif opcao_menu == '2':  # Consultar Livro
            consultar_livro()
        elif opcao_menu == '3':  # Remover Livro
            remover_livro()
        elif opcao_menu == '4':  # Encerrar Programa
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida!")

def main():
    run()

if __name__ == "__main__":
    main()


