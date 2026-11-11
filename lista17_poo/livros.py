class Livro:
    def __init__(self, nome, qtdPaginas, autor, preco):
        self.nome = nome
        self.qtdPaginas = qtdPaginas
        self.autor = autor
        self.preco = preco

    def get_nome(self):
        return self.nome

    def get_qtdPaginas(self):
        return self.qtdPaginas

    def get_autor(self):
        return self.autor

    def get_preco(self):
        return self.preco

    def set_nome(self, nome):
        self.nome = nome

    def set_qtdPaginas(self, qtdPaginas):
        self.qtdPaginas = qtdPaginas

    def set_autor(self, autor):
        self.autor = autor

    def set_preco(self, preco):
        self.preco = preco

livro1 = Livro('abc', 123, 'def', 45)

print(livro1.get_preco())

livro1.set_preco(80)

print(livro1.get_preco())
