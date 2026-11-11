class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.quantCombustivel = 0

    def andar(self, distancia):
        self.quantCombustivel -= distancia / self.consumo

    def obterGasolina(self):
        print(self.quantCombustivel)

    def adicionarGasolina(self, litros):
        self.quantCombustivel += litros

fusca = Carro(15)
fusca.adicionarGasolina(20)
fusca.andar(100)
fusca.obterGasolina()
