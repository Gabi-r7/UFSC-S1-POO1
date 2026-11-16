class Cachorro:
    PRECO_POR_BANHO = 25.0

    def __init__(self, raca, peso, nome, banhos):
        self.raca = raca
        self.peso = peso
        self.nome = nome
        self.banhos = banhos
        self.mensalidade = Cachorro.getMensalidade(self, banhos)

    def getInfo(self):
        print(
            f'Nome: {self.nome}\n'
            f'Raça: {self.raca}\n'
            f'Peso: {self.peso:.2f} kg\n'
            f'Mensalidade: R$ {self.mensalidade:.2f}'
        )

    def getRestricaoAlimentar(self):
        return False

    def getMensalidade(self, banhos=None):
        if banhos is None:
            banhos = self.banhos

        adicional = 0
        if self.peso > 20:
            adicional += 0.10
        if self.raca.lower() in ('pitbull', 'pinscher'):
            adicional += 0.15

        return banhos * self.PRECO_POR_BANHO * (1 + adicional)


class CachorroVip(Cachorro):
    def __init__(self, raca, peso, nome, banhos, restricaoAlimentar):
        super().__init__(raca, peso, nome, banhos)
        self.restricaoAlimentar = restricaoAlimentar
        self.mensalidade = self.getMensalidade()

    def getInfo(self):
        print(
            f'Nome: {self.nome}\n'
            f'Raça: {self.raca}\n'
            f'Peso: {self.peso:.2f} kg\n'
            f'Mensalidade: R$ {self.mensalidade:.2f}\n'
            f'Restrição Alimentar: {self.restricaoAlimentar}'
        )

    def getRestricaoAlimentar(self):
        return self.restricaoAlimentar

    def getMensalidade(self, banhos=None):
        if banhos is None:
            banhos = self.banhos
        return super().getMensalidade(banhos) * 0.80


def cachorroMaisPesado(cachorros):
    """Retorna o cachorro de maior peso da coleção informada."""
    if not cachorros:
        raise ValueError('A lista de cachorros não pode estar vazia.')
    return max(cachorros, key=lambda cachorro: cachorro.peso)


def menu():
    cachorros = []

    while True:
        print('\n1-Cadastrar  2-Informações  3-Restrição')
        print('4-Mensalidade  5-Mais pesado  0-Sair')
        opcao = input('Opção: ')

        if opcao == '1':
            nome = input('Nome: ')
            raca = input('Raça: ')
            peso = float(input('Peso: '))
            banhos = int(input('Banhos por mês: '))
            vip = input('É VIP? (s/n): ').lower() == 's'

            if vip:
                restricao = input('Possui restrição? (s/n): ').lower() == 's'
                cachorro = CachorroVip(raca, peso, nome, banhos, restricao)
            else:
                cachorro = Cachorro(raca, peso, nome, banhos)
            cachorros.append(cachorro)
            print('Cachorro cadastrado.')
        elif opcao == '5':
            if cachorros:
                cachorro = cachorroMaisPesado(cachorros)
                print(f'{cachorro.nome} é o mais pesado: {cachorro.peso:.2f} kg.')
            else:
                print('Nenhum cachorro foi cadastrado.')
        elif opcao == '0':
            break
        elif opcao in ('2', '3', '4') and cachorros:
            for i, cachorro in enumerate(cachorros, 1):
                print(i, '-', cachorro.nome)
            cachorro = cachorros[int(input('Número do cachorro: ')) - 1]

            if opcao == '2':
                cachorro.getInfo()
            elif opcao == '3':
                print(cachorro.getRestricaoAlimentar())
            elif opcao == '4':
                print(f'R$ {cachorro.getMensalidade():.2f}')
        elif opcao in ('2', '3', '4'):
            print('Cadastre um cachorro primeiro.')
        else:

            print('Opção inválida.')

if __name__ == '__main__':
    menu()
