# Variável global
lista_livros = []

def boas_vindas():
    # Mensagem de boas-vindas
    print("================================================")
    print("Bem-vindo ao sistema de gerenciamento de livros!")
    print("================================================")

# Função para cadastrar um livro na lista de livros
def cadastrar_livro(id):
    id_livro = id
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    editora = input("Digite o nome da editora: ")

    livro = {"id": id, "nome": nome, "autor": autor, "editora": editora}
    lista_livros.append(livro)
    print("\n>>> Livro cadastrado com sucesso!")
    print(33*"-", "\n")
    id_livro += 1

# Função para consultar livros
def consultar_livro():
    while True:
        print("\n__Opções de consulta__")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Autor")
        print("4. Retornar ao menu")
        opcao = input("\nEscolha uma opção: ")
        print(18*"-", "\n")

        if opcao == '1':  # Consultar Todos
            print("\n>>> Todos os livros:")
            for livro in lista_livros:
                print("> ", livro)
        elif opcao == '2':  # Consultar por Id
            id_busca = int(input("\nDigite o Id do livro: "))
            for livro in lista_livros:
                if livro["id"] == id_busca:
                    print("Livro encontrado:")
                    print("> ", livro)
                    break
            else:
                print("\nLivro não encontrado.")
                print(15*"+")
        elif opcao == '3':  # Consultar por Autor
            autor_busca = input("\nDigite o nome do autor: ")
            for livro in lista_livros:
                if livro["autor"] == autor_busca:
                    print("> ", livro)
                    break
            else:
                print("\n>>> Nenhum livro encontrado para esse autor.")
        elif opcao == '4':  # Retornar ao menu
            break
        else:
            print("\nOpção inválida!")
            print(15*"+")

# Função para remover um livro da lista de livros
def remover_livro():
    id_remover = int(input("Digite o Id do livro a ser removido: "))
    for livro in lista_livros:
        if livro["id"] == id_remover:
            lista_livros.remove(livro)
            print("\n>>> Livro removido com sucesso!")
            break
    else:
        print("Id inválido. Livro não encontrado.")

def run():
    # Mensagem de boas-vindas
    boas_vindas()

    # Menu principal
    while True:
        print("\n__Opções__")
        print("1. Cadastrar Livro")
        print("2. Consultar Livro")
        print("3. Remover Livro")
        print("4. Encerrar Programa")
        opcao_menu = input("\n>>> Escolha uma opção: ")
        print(25*"-", "\n")

        if opcao_menu == "1":  # Cadastrar Livro
            cadastrar_livro(id=1)
        elif opcao_menu == "2":  # Consultar Livro
            consultar_livro()
        elif opcao_menu == "3":  # Remover Livro
            remover_livro()
        elif opcao_menu == "4":  # Encerrar Programa
            print("\nEncerrando o programa...\n")
            break
        else:
            print("\nOpção inválida!")
            print(15*"+")

def main():
    run()

if __name__ == "__main__":
    main()
