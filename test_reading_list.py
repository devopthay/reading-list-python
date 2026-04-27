import unittest
from reading_list import ReadingList

class TestReadingList(unittest.TestCase):

    def setUp(self):
        self.lista = ReadingList()

    def test_adicionar_livro(self):
        self.lista.add_book("Livro A")
        self.assertIn("Livro A", self.lista.books)

    def test_remover_livro(self):
        self.lista.add_book("Livro B")
        self.lista.remove_book("Livro B")
        self.assertNotIn("Livro B", self.lista.books)

    def test_lista_vazia(self):
        self.assertEqual(len(self.lista.books), 0)

    def test_adicionar_varios_livros(self):
        self.lista.add_book("Livro 1")
        self.lista.add_book("Livro 2")
        self.assertEqual(len(self.lista.books), 2)

    def test_remover_livro_inexistente(self):
        self.lista.remove_book("Livro X")
        self.assertEqual(len(self.lista.books), 0)

if __name__ == "__main__":
    unittest.main()
