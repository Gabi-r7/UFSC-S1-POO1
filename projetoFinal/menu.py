isVendedor = False
escolha = -1
menu1escolha = -1
menu2escolha = -1

while escolha != 0:

    escolha = int(input('\n==================== Bem vindo ao eCommerce ====================\n1 - Menu de usuários\n2 - Menu de produtos\n0 - Sair\nDigite sua escolha: '))

    if escolha == 1:
        while menu1escolha != 0:
            menu1escolha = int(input('-------------------- Menu de usuários --------------------\n1 - Cadastrar novo usuário\n2 - Verificar compradores\n3 - Verificar vendedores\n0 - Voltar ao menu principal\nDigite sua escolha: '))
            if menu1escolha == 1:
                print('Cadastro de funcionário')
                idF += 1
                nome = str(input('Nome: '))
                email = str(input('Email: '))
                endereco = str(input('Endereço: '))

                
                #adicionar a classe
                escolha = 0
            elif escolha == 2:
                pass
            elif escolha == 3:
                pass

    elif escolha == 2:
        while menu2escolha != 0:
            menu2escolha = int(input('-------------------- Menu de produtos --------------------\n1 - Visualizar produtos\n2 - Adicionar um produto aos favoritos\n3 - Adicionar um produto ao carrinho\n0 - Voltar para o menu anterior\nDigite sua escolha: '))
            if menu2escolha == 1:
                pass
            elif menu2escolha == 2:
                pass
            elif menu2escolha == 3:
                pass

    elif escolha == 0:
        escolha = int(input('Tem certeza que você quer encerrar o programa? Digite 0 para continuar ou qualquer número para cancelar: '))
    else:
        pass

compradores = [] # lista de funcionários
vendedores = []
idF = 0

flag=False

#f = Funcionario(str(idF), 'João', '123.456.789-10', 'M') # cria uma instância de Funcionário
#funcionarios.append(f)  # Adiciona o funcionário na lista

while True:
    print('\nMenu de funcionários')
    print('Escolha uma operação para realizar: ')
    print('1 - Cadastrar funcionário')
    print('2 - Alterar informação de funcionário')
    print('3 - Consultar (nome, cpf ou ID)')
    print('4 - Excluir funcionário')
    print('5 - Encerrar execução')
    op = int(input('Escolha uma operação: ')) # o usuário escolhe a opção

    if op == 1: # Operação 1 - Cadastrar
        print('Cadastro de funcionário')
        
        idF += 1
        nome = str(input('Nome: '))
        cpf = str(input('CPF: '))
        sexo = str(input('Sexo: '))
        
        f = Funcionario('', '', '', '') # cria o objeto Funcionario
        f.set_id(str(idF))
        f.set_nome(nome)
        f.set_cpf(cpf)
        f.set_sexo(sexo)

        funcionarios.append(f)  # adiciona na lista de funcionários
        
    elif op == 2: # Operação 2 - Alterar (pelo ID)
        print('Alterar informação de usuário')
        idF = str(input('Digite o ID do funcionário: '))
        flag=False
        for func in funcionarios:  # percorre a lista de funcionários
            if idF == func.get_id():  # busca pelo ID do funcionário a ser alterado
                print('Digite as novas informações do usuário')
                nome = str(input('Nome: '))
                cpf = str(input('CPF: '))
                sexo = str(input('Sexo: '))
               
                func.set_nome(nome) # altera os dados do funcionário
                func.set_cpf(cpf)
                func.set_sexo(sexo)
                flag=True
        if flag == False:
            print("ID não encontrado!")
        
    elif op == 3: # Operação 3 - Consultar
        print('Consultar funcionário')
        print('1 - Consultar pelo ID')
        print('2 - Consultar pelo nome')
        print('3 - Consultar pelo CPF')
        consulta = int(input('Escolha a forma de consulta: '))
        
        if consulta == 1: # Consultar pelo ID
            flag=False
            c = str(input('Digite o ID: '))
            for func in funcionarios:
                if c == func.get_id():
                    print('ID:', func.get_id())  # resgata os dados do funcionário
                    print('Nome:', func.get_nome())
                    print('CPF:', func.get_cpf())
                    print('Sexo:', func.get_sexo())
                    flag = True
            if flag == False:
                print("ID não cadastrado!")
                
                    
        elif consulta == 2: # Consultar pelo Nome
            c = str(input('Digite o nome: '))
            flag = False
            for func in funcionarios:
                if c == func.get_nome():
                    print('ID:', func.get_id())  # resgata os dados do funcionário
                    print('Nome:', func.get_nome())
                    print('CPF:', func.get_cpf())
                    print('Sexo:', func.get_sexo())
                    flag = True
            if flag == False:
                print("Funcionário não cadastrado!")
            
        else:  # consultar pelo CPF
            c = str(input('Digite o CPF: '))
            flag=False
            for func in funcionarios:
                if c == func.get_cpf():
                    print('ID:', func.get_id())  # resgata os dados do funcionário
                    print('Nome:', func.get_nome())
                    print('CPF:', func.get_cpf())
                    print('Sexo:', func.get_sexo())
                    flag = True
            if flag == False:
                print("CPF não cadastrado!")
                    
    elif op == 4: # Excluir funcionário (pelo ID)
        print('Excluir funcionário')
        idF = str(input('Digite o ID do funcionário: '))
        
        for i, j in enumerate(funcionarios): # percorre a lista de funcionários
            if idF == j.get_id():
                funcionarios.pop(i)
                print("Exclusão efetuada com sucesso!")
                flag=True
        if flag == False:
            print("Id não cadastrado!")
    else:
        break