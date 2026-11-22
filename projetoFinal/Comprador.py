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
        if produto_id not in self.carrinho or produto_id not in produtos.values():
            return False

        produto = produtos[produto_id]
        if produto.estoque < quantidade:
            print(f"Estoque insuficiente para {produto.nome}.")
            return False

        self.carrinho.remove(produto_id)
        self.compras.append(produtos[produto_id])
        self.valorGasto += produtos[produto_id].preco

        if produto.vendedor is not None:
            produto.vendedor.Faturar(produto, quantidade)
        return True

    def FinalizarCarrinho(self, produtos):
        for produto_id in list(self.carrinho):
            self.Comprar(produto_id, produtos, quantidade=1)

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
            for p in produtos:
                if p.iden == produto_id:
                    aux.append(p)
                    break
        return aux

    def GetCompras(self):
        return self.compras

    def GetFavoritos(self):
        return self.favoritos