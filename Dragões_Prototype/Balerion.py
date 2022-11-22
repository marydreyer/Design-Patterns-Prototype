from Dragoes import Dragao_Prototype
import copy
import time

class Balerion(Dragao_Prototype):
    def __init__(self, altura, cor, peso, sexo, potenciaDracarys):
        super().__init__()
        time.sleep(1)
        self.altura = altura
        self.cor = cor
        self.peso = peso
        self.sexo = sexo
        self.potenciaDracarys = potenciaDracarys

    def getInformacoes(self):
        return super().getInformacoes() + f"\nPotencia Destruição Dracarys: {self.potenciaDracarys}"

    def clone(self):
        return copy.deepcopy(self)