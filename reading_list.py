class ReadingList:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)


if __name__ == "__main__":
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
