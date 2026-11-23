#VENDEDOR
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

        if isinstance(produtos, dict):
            if prod.iden not in [item['ID'] for item in self.produtos]:
                self.produtos.append(dic)
            produtos[prod.iden] = prod
        else:
            if prod not in produtos:
                self.produtos.append(dic)
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

        if produto.estoque < quantidade:
            print(f"Estoque insuficiente para o produto {produto.nome}.")
            return False

        total = produto.preco * quantidade
        self.faturamento += total
        self.vendas.append({"produto_id": produto.iden, "produto_nome": produto.nome, "quantidade": quantidade, "valor": total})
        self.atualizaEstoque(produto, produto.estoque - quantidade)
        return True

    def VerProdutosVendedor(self):
        if not self.produtos:
            print(f"Você não possui produtos cadastrados.")
            return []

        print(f"Produtos:")
        for item in self.produtos:
            print(f"ID: {item['ID']} | Nome: {item['Nome']} | "f"Categoria: {item['Categoria']} | Preço: R$ {item['Preço']:.2f} | "f"Estoque: {item['Estoque']}")
        return self.produtos

    def Comprar(self, produto_id, produtos, quantidade):
            if produto_id not in self.carrinho:
                return False
    
            if produto_id not in produtos:
                return False
    
            if produtos[produto_id].vendedor == self.iden:
                print('Não é possível comprar seu próprio produto.')
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
