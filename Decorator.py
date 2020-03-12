from abc import ABC, abstractmethod

class Raspado(ABC):
    @abstractmethod
    def precio(self):
        pass
    
class Cliente(Raspado):
    print('Compra Raspado')

class IngredientesExtras(Raspado, ABC):
    def __init__(self, raspado):
        self._raspado = raspado

    @abstractmethod
    def precio(self):
        pass

class Angel(IngredientesExtras):
    def precio(self):
        self._raspado.precio()
    

class Diablito(IngredientesExtras):
    def precio(self):
        self._raspado.precio()


class RaspadoNormal(Raspado):
    def precio(self):
        print('Precio normal de un raspado.')

def main():
    concrete_raspado = RaspadoNormal()
    concrete_raspado_a = Angel(concrete_raspado)
    concrete_raspado_b = Diablito(concrete_raspado)
    concrete_raspado_b.precio()


if __name__ == "__main__":
    main()
