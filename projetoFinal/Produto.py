#produto
class Produto:
    def __init__(self, nome, iden, categoria, preco, estoque, vendedor):
        self.nome = nome
        self.iden = iden
        self.categoria = categoria
        self.preco = preco
        self.estoque = estoque
        self.vendedor = vendedor
    
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
    
a1 = Produto('João', 123, 'Eletrodoméstico', 120, 10, 0)
a2 = Produto('aaaa', 12, 'Eletrodoméstico', 100, 5, 0)

#for i in range(len(a1.getInfo())):
    #print(f'{lista[i]}: {a1.getInfo()[i]}')