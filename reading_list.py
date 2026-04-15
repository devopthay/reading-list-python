print("Lista de leitura")

livros = []

print("1 - Adicionar livro")
print("2 - Listar livros")
print("3 - Marcar como lido")
print("4 - Remover livro")
print("5 - Sair")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    livro = input("Digite o nome do livro: ")
    livros.append(livro)
    print("Livro adicionado com sucesso!")
