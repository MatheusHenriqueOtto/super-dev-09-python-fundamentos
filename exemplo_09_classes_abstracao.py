from abc import ABC, abstractmethod

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