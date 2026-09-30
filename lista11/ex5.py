futebol = set()
natacao = set()
volei = set()
basquete = set()

option = 1

while True:
    option = int(input('-----------------------------------------\nDigite:\n1 Para mostrar a relação de alunos matriculados\n2 Para matricular novos alunos\n3 Para verificar direito ao desconto\n4 Para indicar o total de alunos\n0 para sair\nSua opção: '))
    if option == 0:
        break

    if option == 1:
        print(f'Futebol: {futebol}')
        print(f'Natacao: {natacao}')
        print(f'Volei: {volei}')
        print(f'Basquete: {basquete}')

    elif option == 2:
        esporte = int(input('Digite:\n1 Para Futebol\n2 Para Natacao\n3 Para Volei\n4 Para Basquete\nSua opção: '))
        
        if esporte == 1:
            futebol.add(input('Digite o nome do aluno: '))
        elif esporte == 2:
            natacao.add(input('Digite o nome do aluno: '))
        elif esporte == 3:
            volei.add(input('Digite o nome do aluno: '))
        elif esporte == 4:
            basquete.add(input('Digite o nome do aluno: '))

    elif option == 3:
        aluno = input('Digite o nome do aluno: ')

        if (aluno in futebol and aluno in natacao) or (aluno in futebol and aluno in volei) or (aluno in futebol and aluno in basquete) or (aluno in natacao and aluno in volei) or (aluno in natacao and aluno in basquete) or (aluno in volei and aluno in basquete):
            print(f'O aluno {aluno} tem direito ao desconto')
        else:
            print(f'O aluno {aluno} não tem direito ao desconto')
    
    elif option == 4:
        total_alunos = len(futebol.union(natacao, volei, basquete))
        print(f'Total de alunos: {total_alunos}')
        print(f'Total Futebol: ', len(futebol))
        print(f'Total Natacao: ', len(natacao))
        print(f'Total Volei: ', len(volei))
        print(f'Total Basquete: ', len(basquete))
    else:
        print('Opção inválida')

    input('Pressione Enter para continuar...')
