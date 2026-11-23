#PRODUTO
class Produto:
    def __init__(self, nome, iden, categoria, preco, estoque, vendedor=None):
        self.nome = nome
        self.iden = iden
        self.categoria = categoria
        self.preco = preco
        self.estoque = estoque
        self.vendedor = vendedor

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return (
            f'ID: {self.iden} | Nome: {self.nome} '
            f'| Categoria: {self.categoria} | Preco: R$ {self.preco:.2f} '
            f'| Estoque: {self.estoque}'
        )

    def __repr__(self):
        return str(self)
    
    def getID(self):
        return self.iden
    
    def getCat(self):
        return self.categoria
        
    def getPreco(self):
        return self.preco
    
    def getEstoque(self):
        return self.estoque
    
    def getInfo(self):
        return self.nome, self.iden, self.categoria, self.preco, self.estoque
    