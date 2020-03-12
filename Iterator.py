from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List

class Orden_Alfabetico(Iterator):

    _posicion: int = None

    _reverse: bool = False

    def __init__(self, collection: Palabras, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._posicion = -1 if reverse else 0

    def __next__(self):

        try:
            value = self._collection[self._posicion]
            self._posicion += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        

        return value


class Palabras(Iterable):

    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> Orden_Alfabetico:

        return Orden_Alfabetico(self._collection)

    def get_reverse_iterator(self) -> Orden_Alfabetico:
        return Orden_Alfabetico(self._collection, True)

    def agregar_letra(self, item: Any):
        self._collection.append(item+".jpg")


if __name__ == "__main__":

    collection = Palabras()
    collection.agregar_letra("A")
    collection.agregar_letra("B")
    collection.agregar_letra("C")
    collection.agregar_letra("D")
    collection.agregar_letra("E")

    print("\n".join(collection.get_reverse_iterator())[12:17] )









    

