from datetime import date


usuarios = {}

while True:
    print('\na - Cadastrar usuário')
    print('b - Imprimir dados (pesquisar pelo nome)')
    print('c - Imprimir dados (todos os usuários)')
    print('d - Encerrar o programa')

    opcao = input('Escolha uma opção: ').lower()

    if opcao == 'a':
        nome = input('Nome: ')
        ano_nascimento = int(input('Ano de nascimento: '))
        carteira = int(input('Carteira de trabalho (0 se não possui): '))

        pessoa = {
            'nome': nome,
            'idade': date.today().year - ano_nascimento,
            'carteira de trabalho': carteira
        }

        if carteira != 0:
            ano_contratacao = int(input('Ano de contratação: '))
            salario = float(input('Salário: '))
            idade_aposentadoria = ano_contratacao - ano_nascimento + 35

            pessoa['ano de contratação'] = ano_contratacao
            pessoa['salário'] = salario
            pessoa['idade de aposentadoria'] = idade_aposentadoria

        usuarios[nome] = pessoa
        print('Usuário cadastrado.')

    elif opcao == 'b':
        nome = input('Nome para pesquisa: ')

        if nome in usuarios:
            print(usuarios[nome])
        else:
            print('Usuário não encontrado.')

    elif opcao == 'c':
        if len(usuarios) == 0:
            print('Nenhum usuário cadastrado.')
        else:
            for pessoa in usuarios.values():
                print(pessoa)

    elif opcao == 'd':
        print('Programa encerrado.')
        break

    else:
        print('Opção inválida.')