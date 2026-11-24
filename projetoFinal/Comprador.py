#COMPRADOR
class Comprador:
    def __init__(self, nome, senha, iden, email, endereco):
        self.nome = nome
        self.senha = senha
        self.iden = iden
        self.email = email
        self.endereco = endereco
        self.carrinho = []
        self.compras = []
        self.favoritos = []
        self.valorGasto = 0.0

    def Comprar(self, produto_id, produtos, quantidade):
        if produto_id not in self.carrinho:
            return False

        if produto_id not in produtos:
            return False

        produto = produtos[produto_id]
        if quantidade <= 0:
            print('Quantidade invalida.')
            return False

        if produto.estoque < quantidade:
            print(f"Estoque insuficiente para {produto.nome}.")
            return False

        self.carrinho.remove(produto_id)
        self.compras.append(produto)
        self.valorGasto += produto.preco * quantidade

        if produto.vendedor is not None:
            return produto.vendedor.Faturar(produto, quantidade)
        return True

    def FavoritarProduto(self, produto_id):
        if produto_id in self.favoritos:
            return False

        self.favoritos.append(produto_id)
        return True

    def AdicionarCarrinho(self, produto_id):
        if produto_id in self.carrinho:
            print('Produto já foi adicionado anteriormente ao carrinho. ')
            return False

        self.carrinho.append(produto_id)
        return True

    def RemoverCarrinho(self, produto_id):
        if produto_id not in self.carrinho:
            print('Produto não está no carrinho. ')
            return False

        self.carrinho.remove(produto_id)
        return True

    def GetCarrinho(self, produtos):
        aux = []
        for produto_id in self.carrinho:
            if produto_id in produtos:
                aux.append(produtos[produto_id])
        return aux

    def GetFavoritos(self):
        return self.favoritos