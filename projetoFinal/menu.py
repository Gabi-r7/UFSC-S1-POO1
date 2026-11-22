import time
from Comprador import Comprador
from Produto import Produto
from Vendedor import Vendedor

compradores = []
vendedores = []
produtos = []

compradores = [
    Comprador("Ana", "123", 1, "ana@email.com", "Rua das Flores"),
    Comprador("Carlos", "123", 2, "carlos@email.com", "Centro"),
    Comprador("Loja sla", "123", 3, "loja@email.com", "Rua da Loja")
]

vendedores = [
    Vendedor("Loja Tech", "123", 4, "lojatech@email.com", "Rua da Loja")
]

# Como vendedor herda comprador, adicione-o também nesta lista
compradores.append(vendedores[0])

produtos = {
    0: Produto("Notebook", 0, "Informática", 3500.0, 5, vendedores[0]),
    1: Produto("Mouse", 1, "Informática", 80.0, 20, vendedores[0]),
    2: Produto("Camiseta", 2, "Vestuário", 50.0, 15, vendedores[0]),
    3: Produto("Café", 3, "Alimentos", 25.0, 30, vendedores[0])
}

for produto in produtos.values():
    vendedores[0].addProduto(produto, produtos)

isVendedor = False
idF = 0
idP = max(produtos.keys(), default=-1) + 1
usuario_atual = None
escolha = -1
menu1escolha = -1
menu2escolha = -1

while escolha != 0:

    escolha = int(input("\033[32m==================== Bem vindo ao eCommerce ====================\n1 - Menu de usuários\n2 - Menu de produtos\n0 - Sair\nDigite sua escolha: \033[0m"))

    if escolha == 1:
        menu1escolha = -1
        while menu1escolha != 0:
            menu1escolha = int(input('\n-------------------- Menu de usuários --------------------\n1 - Cadastrar novo usuário\n2 - Fazer login\n3 - Verificar compradores\n4 - Verificar vendedores\n5 - Deslogar\n0 - Voltar ao menu principal\nDigite sua escolha: '))
            if menu1escolha == 1:
                print('Cadastro de usuário')
                idF += 1
                nome = str(input('Nome: '))
                email = str(input('Email: '))
                senha = str(input('Senha: '))
                endereco = str(input('Endereço: '))
                tipo = str(input('Tipo (comprador/vendedor): ')).lower()

                if tipo == 'comprador':
                    usuario = Comprador(nome, senha, idF, email, endereco)
                    compradores.append(usuario)
                    print('Usuário cadastrado com sucesso!')
                    time.sleep(1)
                elif tipo == 'vendedor':
                    usuario = Vendedor(nome, senha, idF, email, endereco)
                    compradores.append(usuario)
                    vendedores.append(usuario)
                    print('Usuário cadastrado com sucesso!')
                    time.sleep(1)
                else:
                    print('Tipo de usuário inválido. Por favor, escolha "comprador" ou "vendedor".')
                    time.sleep(1)
                    continue

            elif menu1escolha == 2 and usuario_atual is None:
                email = str(input('Email: '))
                senha = str(input('Senha: '))

                usuario_atual = None
                for comprador in compradores:
                    if comprador.email == email and comprador.senha == senha:
                        usuario_atual = compradores[compradores.index(comprador)]
                        break

                if usuario_atual is not None:
                    print(f'Login bem-sucedido! Bem-vindo, {usuario_atual.nome}.')
                    time.sleep(1)
                else:
                    print('Email ou senha incorretos. Tente novamente.')
                    time.sleep(1)

            elif menu1escolha == 3 and usuario_atual is not None:
                if not isinstance(usuario_atual, Vendedor):
                    print('Você é um comprador.')
                    time.sleep(1)
                else:
                    if len(compradores) == 0:
                        print('Não há compradores cadastrados.')
                        time.sleep(1)
                    else:
                        print('Lista de compradores:')
                        for comprador in compradores:
                            print(f'ID: {comprador.iden}, Nome: {comprador.nome}, Email: {comprador.email}, Endereço: {comprador.endereco}')
                
            elif menu1escolha == 4 and usuario_atual is not None:
                if isinstance(usuario_atual, Comprador) and isinstance(usuario_atual, Vendedor):
                    print('Você é um vendedor.')
                    time.sleep(1)
                else:
                    if len(vendedores) == 0:
                        print('Não há vendedores cadastrados.')
                        time.sleep(1)
                    else:
                        print('Lista de vendedores:')
                        for vendedor in vendedores:
                            print(f'ID: {vendedor.iden}, Nome: {vendedor.nome}, Email: {vendedor.email}, Endereço: {vendedor.endereco}')

            elif menu1escolha == 5 and usuario_atual is not None:
                usuario_atual = None
                print('Usuário deslogado. ')
                time.sleep(1)

            else:
                if menu1escolha == 0:
                    break
                elif usuario_atual is None and menu1escolha in [3, 4, 5]:
                    print('Você precisa estar logado para acessar essa opção.')
                    time.sleep(1)
                else:
                    print('Opção inválida. Por favor, escolha uma opção válida.')
                    time.sleep(1)
                continue

    
    elif escolha == 2:
        menu2escolha = -1
        while menu2escolha != 0:
               
            print('-------------------- Menu de produtos --------------------\n1 - Visualizar produtos\n2 - Adicionar um produto aos favoritos\n3 - Filtro de produtos\n4 - Opções do carrinho\n0 - Voltar para o menu anterior')

            if isinstance(usuario_atual, Vendedor):
                print('5 - Ver seus produtos (vendedor)\n6 - Adicionar produto (vendedor)\n7 - Atualizar preço do produto (vendedor)\n8 - Atualizar estoque do produto (vendedor)\n9 - Ver faturamento (vendedor)')
    
            menu2escolha = int(input('Digite sua escolha: '))

            if menu2escolha == 1: 
                if len(produtos) == 0:
                    print('Não há produtos disponíveis.')
                    time.sleep(1)
                    continue
                else:
                    print('Lista de produtos disponíveis:')
                    for produto in produtos.values():
                        print(f'ID: {produto.iden} | Nome: {produto.nome} | Categoria: {produto.categoria} | Preço: {produto.preco} | Estoque: {produto.estoque}\n')
                time.sleep(1)
            elif menu2escolha == 2 and usuario_atual is not None:
                idAux = int(input('Digite o ID do produto que deseja adicionar aos favoritos: '))
                produto_encontrado = None

                for produto in produtos.values():
                    if produto.iden == idAux:
                        produto_encontrado = produto
                        break
            
                if produto_encontrado is not None:
                    if usuario_atual is not None:
                        if usuario_atual.FavoritarProduto(produto_encontrado.iden):
                            print(f'Produto {produto_encontrado.nome} adicionado aos favoritos.')
                            time.sleep(1)
                        else:
                            print('Produto já está nos favoritos.')
                            time.sleep(1)
                    else:
                        print('Você precisa estar logado para favoritar produtos.')
                        time.sleep(1)
                else:
                    print('Produto não encontrado.')
                    time.sleep(1)
            
            elif menu2escolha == 3:
                auxFiltro = int(input('Escolha o filtro de produtos:\n1 - Filtrar por categoria\n2 - Filtrar por preço\nDigite sua escolha: '))
                if auxFiltro == 1:
                    categoria = str(input('Digite a categoria desejada: '))
                    for produto in produtos.values():
                        if produto.categoria.lower() == categoria.lower():
                            print(f'ID: {produto.iden}, Nome: {produto.nome}, Categoria: {produto.categoria}, Preço: {produto.preco}, Estoque: {produto.estoque}')
                
                elif auxFiltro == 2:
                    preco_max = float(input('Digite o preço máximo: '))
                    for produto in produtos.values():
                        if produto.preco <= preco_max:
                            print(f'ID: {produto.iden}, Nome: {produto.nome}, Categoria: {produto.categoria}, Preço: {produto.preco}, Estoque: {produto.estoque}')

            elif menu2escolha == 4 and usuario_atual is not None:
                opcao_carrinho = int(input('Opções de Carrinho: \n1 - Ver carrinho\n2 - Adicionar ao carrinho\n3 - Remover do carrinho\n4 - Comprar carrinho\nDigite sua escolha: '))

                if opcao_carrinho == 1:
                    print('Carrinho: ')
                    print(usuario_atual.GetCarrinho(produtos))
                elif opcao_carrinho == 2:
                    prod_add = int(input('Digite o ID do produto a ser adicionado do carrinho: '))
                    for produto in produtos.values():
                        if produto.iden == prod_add and produto.estoque > 0 and usuario_atual.AdicionarCarrinho(prod_add):
                            print(f'O produto {produto.nome} foi adicionado com sucesso. ')
                            time.sleep(1)
                            break
                    else:
                        print('Produto não encontrado.')
                        time.sleep(1)
                        continue
                    
                elif opcao_carrinho == 3:
                    prod_rmv = int(input('Digite o ID do produto a ser removido do carrinho: '))
                    for produto in produtos.values():
                        if produto.iden == prod_rmv:
                            if usuario_atual.RemoverCarrinho(prod_rmv):
                                print(f'O produto {produto.nome} foi removido com sucesso. ')
                            else:
                                print('Produto não está no carrinho.')
                            time.sleep(1)
                            break
                    else:
                        print('Produto não encontrado.')
                        time.sleep(1)
                        continue
                
                
                elif opcao_carrinho == 4:
                    carrinho = usuario_atual.GetCarrinho(produtos)
                    if len(carrinho) == 0:
                        print('O carrinho está vazio.')
                        time.sleep(1)
                        continue

                    for produto in list(carrinho):
                        quantidade = int(input(
                            f'Digite a quantidade de "{produto.nome}" a ser comprada: '
                        ))

                        if quantidade <= 0:
                            print('Quantidade inválida. Operação cancelada.')
                            time.sleep(1)
                            continue

                        if produto.estoque < quantidade:
                            print(
                                f'Estoque insuficiente para o produto {produto.nome}. '
                                f'Estoque atual: {produto.estoque}.'
                            )
                            time.sleep(1)
                            continue

                        if usuario_atual.Comprar(produto.iden, produtos, quantidade):
                            print(f'O produto {produto.nome} foi comprado com sucesso.')
                        else:
                            print(f'Não foi possível comprar o produto {produto.nome}.')
                        time.sleep(1)
                        
                else:
                    print('Opção inválida. Por favor, escolha uma opção válida.')
                    time.sleep(1)
                    continue

            elif isinstance(usuario_atual, Vendedor) and menu2escolha == 5:
                usuario_produtos = usuario_atual.VerProdutosVendedor()

            elif isinstance(usuario_atual, Vendedor) and menu2escolha == 6:
                # Adicionar produto (vendedor)
                nome_add = input('Nome do produto: ')
                categoria_add = input('Digite a categoria do produto: ')
                preco_add = float(input('Digite o preço do produto: '))
                estoque_add = int(input('Digite o estoque atual: '))

                if preco_add < 0 or estoque_add < 0:
                    print('Preço ou estoque inválido. Operação cancelada.')
                    time.sleep(1)
                    continue

                novo_produto = Produto(
                    nome_add,
                    idP,
                    categoria_add,
                    preco_add,
                    estoque_add,
                    usuario_atual
                )
                usuario_atual.addProduto(novo_produto, produtos)
                idP += 1
                print(f'Produto "{novo_produto.nome}" cadastrado com sucesso.')
                time.sleep(1)
            elif isinstance(usuario_atual, Vendedor) and menu2escolha == 7:
                # Atualizar preço do produto (vendedor)
                id_preco = int(input('Digite o ID do produto: '))
                novo_preco = float(input('Digite o novo preço do produto: '))
                produto = produtos.get(id_preco)
                if (
                    produto is None
                    or not any(item['ID'] == id_preco for item in usuario_atual.produtos)
                ):
                    print('Produto não encontrado entre os produtos deste vendedor.')
                    time.sleep(1)
                    continue
                if novo_preco < 0:
                    print('Preço negativo. Operação cancelada.')
                    time.sleep(1)
                    continue
                usuario_atual.atualizaPreco(produto, novo_preco)
                print(f'O preço do produto {produto.nome} foi atualizado para {novo_preco}.')
                time.sleep(1)
                
            elif isinstance(usuario_atual, Vendedor) and menu2escolha == 8:
                # Atualizar estoque do produto (vendedor)
                id_estoque = int(input('Digite o ID do produto: '))
                novo_estoque = int(input('Digite o novo estoque do produto: '))
                produto = produtos.get(id_estoque)
                if (
                    produto is None
                    or not any(item['ID'] == id_estoque for item in usuario_atual.produtos)
                ):
                    print('Produto não encontrado entre os produtos deste vendedor.')
                    time.sleep(1)
                elif novo_estoque < 0:
                    print('Estoque negativo. Operação cancelada.')
                    time.sleep(1)
                else:
                    usuario_atual.atualizaEstoque(produto, novo_estoque)
                    print(f'O estoque do produto {produto.nome} foi atualizado para {novo_estoque}.')
                    time.sleep(1)
            elif isinstance(usuario_atual, Vendedor) and menu2escolha == 9:
                print(f'Faturamento: R$ {usuario_atual.faturamento:.2f}')
                print('Vendas realizadas:')
                if len(usuario_atual.vendas) == 0:
                    print('Nenhuma venda realizada.')
                else:
                    for venda in usuario_atual.vendas:
                        print(
                            f'Produto: {venda["produto_nome"]} | '
                            f'Quantidade: {venda["quantidade"]} | '
                            f'Valor: R$ {venda["valor"]:.2f}'
                        )
                time.sleep(1)
            else:
                if menu2escolha == 0:
                    break
                elif usuario_atual is None and menu2escolha in [2, 4, 5, 6, 7]:
                    print('Você precisa estar logado para acessar essa opção.')
                    time.sleep(1)
                else:
                    print('Opção inválida. Por favor, escolha uma opção válida.')
                    time.sleep(1)
                continue

    elif escolha == 0:
        escolha = int(input('Tem certeza que você quer encerrar o programa? Digite 0 para continuar ou qualquer número para cancelar: '))
    else:
        pass