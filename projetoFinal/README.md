# Projeto Final - Sistema de eCommerce

Este projeto foi desenvolvido como trabalho final da disciplina de **Programação Orientada a Objetos 1**.

## Contexto

O projeto consiste em uma aplicação de console escrita em Python que simula o funcionamento de uma loja virtual. Por meio de menus interativos, o usuário pode cadastrar contas, navegar pelos produtos, utilizar um carrinho de compras e gerenciar produtos como vendedor.

A aplicação funciona em memória, sem banco de dados ou persistência entre execuções. Os dados são armazenados durante o uso do programa em listas, conjuntos e no dicionário de produtos.

## Estrutura do projeto

- `menu.py`: ponto de entrada da aplicação e responsável pela interface com o usuário.
- `Comprador.py`: define os usuários que podem comprar produtos.
- `Vendedor.py`: define os vendedores e amplia as funcionalidades da classe comprador.
- `Produto.py`: representa os produtos disponíveis na loja.

## Classes principais

### Produto

A classe `Produto` representa os itens disponíveis na loja e armazena:

- Nome
- Identificador
- Categoria
- Preço
- Quantidade em estoque
- Vendedor responsável pelo produto

Ela também fornece métodos para consultar identificador, categoria, preço, estoque e informações gerais do produto.

### Comprador

A classe `Comprador` representa um usuário comprador e contém:

- Nome
- Senha
- Identificador
- Email
- Endereço
- Carrinho de compras
- Lista de produtos favoritos
- Valor total gasto

Suas principais funcionalidades são adicionar ou remover produtos do carrinho, favoritar produtos, visualizar o carrinho e finalizar compras.

### Vendedor

A classe `Vendedor` herda da classe `Comprador`, pois um vendedor também pode utilizar a aplicação como comprador.

Além das funcionalidades de comprador, ela armazena os produtos vendidos pelo usuário, o histórico de vendas e o faturamento. O vendedor pode cadastrar produtos, atualizar preço e estoque e consultar suas vendas.

## Principais funcionalidades

### Cadastro e acesso de usuários

- Cadastro de comprador ou vendedor.
- Login por email e senha.
- Logout.
- Listagem dos vendedores cadastrados.
- Identificadores únicos para usuários e produtos.

### Gerenciamento de produtos

- Visualização de todos os produtos disponíveis.
- Filtragem por categoria.
- Filtragem por preço máximo.
- Cadastro de produtos por vendedores.
- Atualização do preço de um produto.
- Atualização da quantidade em estoque.
- Associação automática de um produto ao vendedor que o cadastrou.

### Carrinho e compras

- Adição e remoção de produtos do carrinho.
- Visualização dos produtos presentes no carrinho.
- Escolha da quantidade desejada durante a compra.
- Verificação de estoque antes da finalização.
- Atualização automática do estoque após a venda.
- Impedimento da compra de produtos cadastrados pelo próprio vendedor.

### Favoritos

- Adição de produtos à lista de favoritos.
- Impedimento de adicionar o mesmo produto mais de uma vez.

### Faturamento

- Registro individual das vendas realizadas.
- Cálculo do faturamento de cada vendedor.
- Histórico com nome do produto, quantidade vendida e valor da venda.
- Cálculo do faturamento total de todos os vendedores.

## Conceitos de Programação Orientada a Objetos utilizados

- **Classes e objetos:** compradores, vendedores e produtos são representados por classes.
- **Herança:** `Vendedor` herda atributos e comportamentos da classe `Comprador`.
- **Polimorfismo:** a classe `Vendedor` sobrescreve o método `Comprar` para impedir a compra de seus próprios produtos.
- **Composição:** os produtos podem estar associados ao vendedor responsável pelo seu cadastro.

## Execução

Para executar o projeto a partir da pasta `projetoFinal`:

```bash
python menu.py
```

O programa apresenta menus para usuários e produtos. Por meio deles, é possível cadastrar contas, fazer login, cadastrar vendedores, gerenciar produtos e realizar compras.
