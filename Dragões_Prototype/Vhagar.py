from Dragoes import Dragao_Prototype
import copy
import time

class Vhagar(Dragao_Prototype):
    def __init__(self, altura, cor, peso, sexo, resistenciaVoo ):
        super().__init__()
        time.sleep(1)
        self.altura = altura
        self.cor = cor
        self.peso = peso
        self.sexo = sexo
        self.resistenciaVoo = resistenciaVoo

    def getInformacoes(self):
        return super().getInformacoes() + f"\nResistencia em voo: {self.resistenciaVoo}"

    def clone(self):
        return copy.deepcopy(self)