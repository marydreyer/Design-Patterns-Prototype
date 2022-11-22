from Dragoes import Dragao_Prototype
import copy
import time

class Syrax(Dragao_Prototype):
    def __init__(self, altura, cor, peso, sexo, agilidade):
        super().__init__()
        time.sleep(1)
        self.altura = altura
        self.cor = cor
        self.peso = peso
        self.sexo = sexo
        self.agilidade = agilidade

    def getInformacoes(self):
        return super().getInformacoes() + f"\nAgilidade: {self.agilidade}"

    def clone(self):
        return copy.deepcopy(self)