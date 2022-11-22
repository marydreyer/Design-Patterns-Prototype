from abc import ABCMeta, abstractmethod
import time

class Dragao_Prototype(metaclass=ABCMeta):
    #Construtor
    def __init__(self):
        time.sleep(1)
        self.altura = None
        self.cor = None
        self.peso = None
        self.sexo = None

    def getInformacoes(self):
        return f"Altura: {self.altura}\nCor: {self.cor}\nPeso: {self.peso}\nSexo: {self.sexo}"
    
    @abstractmethod
    def clone(self):
        pass