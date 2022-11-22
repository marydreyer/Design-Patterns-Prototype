from Dragoes import Dragao

class Balerion(Dragao):
    def __init__(self, altura=None, cor=None, peso=None, sexo= None, potenciaDracarys= None):
        super().__init__(altura, cor, peso, sexo)
        self.potenciaDracarys = potenciaDracarys

    def getInformacoes(self):
        return super().getInformacoes() + f"\nPotencia Destruição Dracarys: {self.potenciaDracarys}"

    def cadastrar(self, altura, cor, peso, sexo, potenciaDracarys):
        self.altura = altura
        self.cor = cor
        self.peso = peso
        self.sexo = sexo
        self.potenciaDracarys = potenciaDracarys