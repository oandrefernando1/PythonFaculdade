print("\nBem-vindo ao controle de Livros do Andre Fernando!") # Imprime uma mensagem de boas-vindas
print("****************************************************************")
lista_livro = [] # Inicializa uma lista vazia para armazenar livros

id_global = 1 # Inicializa um contador global para os IDs dos livros

def cadastrar_livro(id): # Define uma função para cadastrar um livro
    print("\n--------------------- MENU CADASTRAR LIVRO ---------------------")
    print("ID do Livro:", id)# Imprime o ID do livro sendo cadastrado
    # Solicita informações do livro ao usuário
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    editora = input("Digite a editora do livro: ")
    # Cria um dicionário para representar o livro e adiciona à lista de livros
    livro = {"ID": id, "Nome": nome, "Autor": autor, "Editora": editora}
    lista_livro.append(livro)

def consultar_livro(): # Define uma função para consultar livros
    while True:
        # Exibe opções de consulta para o usuário
        print("\n----------------------- MENU DE CONSULTA -----------------------")
        print("Opções de Consulta:")
        print("1 - Consultar Todos os livros")
        print("2 - Consultar livro por ID")
        print("3 - Consultar livro por Autor")
        print("4 - Retornar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            if not lista_livro:
                print("Nenhum livro cadastrado!")
            else:
                print("\nLista de Livros:")
                # Exibe detalhes de todos os livros na lista
                for livro in lista_livro:
                    print("\nDetalhes do Livro:")
                    print("ID:", livro["ID"])
                    print("Nome:", livro["Nome"])
                    print("Autor:", livro["Autor"])
                    print("Editora:", livro["Editora"])
        elif opcao == "2":
            id_busca = int(input("Digite o ID do livro: "))
            encontrado = None
            # Procura um livro com o ID especificado
            for livro in lista_livro:
                if livro["ID"] == id_busca:
                    encontrado = livro
                    break
            if encontrado:
                print("\nDetalhes do Livro:")
                print("ID:", encontrado["ID"])
                print("Nome:", encontrado["Nome"])
                print("Autor:", encontrado["Autor"])
                print("Editora:", encontrado["Editora"])
            else:
                print("Livro não encontrado!")
        elif opcao == "3":
            autor_busca = input("Digite o nome do autor: ")
            encontrados = []
            # Procura livros do autor especificado
            for livro in lista_livro:
                if livro["Autor"] == autor_busca:
                    encontrados.append(livro)
            if encontrados:
                print("\nLivros do Autor:")
                # Exibe detalhes dos livros encontrados
                for livro in encontrados:
                    print("\nDetalhes do Livro:")
                    print("ID:", livro["ID"])
                    print("Nome:", livro["Nome"])
                    print("Autor:", livro["Autor"])
                    print("Editora:", livro["Editora"])
            else:
                print("Nenhum livro encontrado para este autor!")
        elif opcao == "4":
            break
        else:
            print("Opção inválida, Tente novamente!")

def remover_livro(): # Define uma função para remover um livro
    print("\n----------------------------------------------------------------")
    id_remover = int(input("Digite o ID do livro para remover: "))
    for livro in lista_livro:
        if livro["ID"] == id_remover:
            lista_livro.remove(livro)
            print("Livro removido com sucesso!")
            break
    else:
        print("Livro não encontrado!")

while True: # Inicia o loop principal do programa
    # Exibe o menu principal para o usuário
    print("------------------------ MENU PRINCIPAL ------------------------")
    print("1 - Cadastrar Livro")
    print("2 - Consultar Livro")
    print("3 - Remover Livro(s)")
    print("4 - Sair")
    opcao_menu = input("Escolha uma opção: ")

    if opcao_menu == "1":
        # Chama a função de cadastro de livros, passando o ID global
        cadastrar_livro(id_global)
        id_global += 1
    elif opcao_menu == "2":
        # Chama a função de consulta de livros
        consultar_livro()
    elif opcao_menu == "3":
        # Chama a função de remoção de livros
        remover_livro()
    elif opcao_menu == "4":
        # Encerra o programa
        print("Encerrando o programa!")
        break
    else:
        print("Opção inválida, Tente novamente!")
