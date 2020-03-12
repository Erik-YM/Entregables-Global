from __future__ import annotations
from abc import ABC, abstractmethod



class AutoOriginal():
    _color = None

    def __init__(self, color: str) -> None:
        self._color = color

    def cambiarColor(self,color) -> None:

        self._color = color

    def guardar(self) -> Memento:
        return ConcreteMemento(self._color)

    def restaurar(self, memento: Memento) -> None:
        self._color = memento.get_color()

class Memento(ABC):
    @abstractmethod
    def get_color(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, state: str) -> None:
        self._color = state

    def get_color(self) -> str:
        return self._color

class Caretaker():
    

    def __init__(self, AutoOriginal: AutoOriginal) -> None:
        self._mementos = []
        self._AutoOriginal = AutoOriginal
        self._lista = []
        

    def backup(self) -> None:
        self._mementos.append(self._AutoOriginal.guardar())


    def undo(self,contadot) -> None:
        return (self._mementos[contadot].get_color() )

    def siguiente(self,contadot) -> None:
        return (self._mementos[contadot].get_color() )
    

if __name__ == "__main__":

    print('Hola')



