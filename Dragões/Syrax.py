from Dragoes import Dragao

class Syrax(Dragao):
    def __init__(self, altura=None, cor=None, peso=None, sexo= None, agilidade= None):
        super().__init__(altura, cor, peso, sexo)
        self._agilidade = agilidade

    def getInformacoes(self):
        return super().getInformacoes() + f"\nAgilidade: {self._agilidade}"

    def cadastrar(self, altura, cor, peso, sexo,agilidade):
        self.altura = altura
        self.cor = cor
        self.peso = peso
        self.sexo = sexo
        self._agilidade = agilidade