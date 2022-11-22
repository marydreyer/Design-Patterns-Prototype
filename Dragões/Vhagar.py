from Dragoes import Dragao

class Vhagar(Dragao):
    def __init__(self, altura=None, cor=None, peso=None, sexo= None, resistenciaVoo= None):
        super().__init__(altura, cor, peso, sexo)
        self._resistenciaVoo = resistenciaVoo

    def getInformacoes(self):
        return super().getInformacoes() + f"\nResistência em horas de voo: {self._resistenciaVoo}"

    def cadastrar(self, altura, cor, peso, sexo, resistenciaVoo):
        self.altura = altura
        self.cor = cor
        self.peso = peso
        self.sexo = sexo
        self._resistenciaVoo = resistenciaVoo