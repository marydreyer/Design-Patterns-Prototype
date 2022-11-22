from abc import ABCMeta, abstractmethod


class Dragao(metaclass=ABCMeta):
    def __init__(self, altura = None, cor = None, peso = None, sexo = None):
        self.altura = altura
        self.cor = cor
        self.peso = peso
        self.sexo = sexo

    def getInformacoes(self):
        return f"Altura: {self.altura}\nCor: {self.cor}\nPeso: {self.peso}\nSexo: {self.sexo}"

    @abstractmethod
    def cadastrar(self):
        pass