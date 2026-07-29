from abc import ABC, abstractmethod
from math import pi

# 1. O MOLDE (contrato) - não pode ser instanciado sozinho
class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass

# 2. As classes concretas OBEDECEM ao contrato
class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

# 3. Testando
cachorro = Cachorro()
gato = Gato()

print(cachorro.fazer_som())  # Au au!
print(gato.fazer_som())      # Miau!

# 4. Isso aqui vai DAR ERRO, pois Animal é só o molde:
animal = Animal()

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self) -> float:
        """Toda forma geométrica deverá implementar uma função para calcular sua area"""
        pass

class Circulo(FormaGeometrica):
    def __init__(self, raio: float):
        self.raio = raio

    def calcular_area(self) -> float:
        area = pi*self.raio**2
        return area


class Quadrado(FormaGeometrica):
    def __init__(self, nome):
        self.nome = nome


        

