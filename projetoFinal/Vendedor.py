from Produto import Produto
from Comprador import Comprador

class Vendedor(Comprador):
    def __init__(self, nome, senha, iden, email, endereco):
        super().__init__(nome, senha, iden, email, endereco)

        self.vendas = []
        self.faturamento = 0.0
        self.produtos = []

    def addProduto(self, prod:Produto, produtos):
        prod.vendedor = self
        dic = {
            'Nome': prod.nome,
            'ID': prod.iden,
            'Categoria': prod.categoria,
            'Preço': prod.preco,
            'Estoque': prod.estoque
        }
        self.produtos.append(dic)

        if isinstance(produtos, dict):
            produtos[prod.iden] = prod
        else:
            produtos.append(prod)
        
    def atualizaEstoque(self, prod, valor):
        if valor < 0:
            print('Estoque negativo. Operação cancelada.')
            return

        for item in self.produtos:
            if item['ID'] == prod.iden:
                item['Estoque'] = valor
                prod.estoque = valor  
                return
        print('Produto não encontrado.')
        
    def atualizaPreco(self, prod, valor):
        if valor < 0:
            print('Preço negativo. Operação cancelada.')
            return

        for item in self.produtos:
            if item['ID'] == prod.iden:
                item['Preço'] = valor
                prod.preco = valor
                return
        print('Produto não encontrado.')

    def Faturar(self, produto: Produto, quantidade: int = 1):
        if produto.preco < 0 or quantidade <= 0:
            return False

        total = produto.preco * quantidade
        self.faturamento += total
        self.vendas.append({
            "produto_id": produto.iden,
            "produto_nome": produto.nome,
            "quantidade": quantidade,
            "valor": total
        })
        self.atualizaEstoque(produto, produto.estoque - quantidade)
        return True

# a5 = Produto('hufdiufduhsi', 1, 'casa', 100, 10)
# b1 = Vendedor('joao', 123, 1, 'email1@gmail.com', 'casa')
# b1.addProduto(a5)
# print(b1.produtos)

# b1.atualizaPreco(a5, 200)
# b1.atualizaEstoque(a5, 10000000)
# print(b1.produtos)