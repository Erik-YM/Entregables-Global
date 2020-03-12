"""
Autor: Erik Yáñez Morin
Fecha:10/12/2019
Franquisia_B
"""
from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any

class Franquisia_B(ABC):
    @abstractproperty
    def nuevaFranquisia(self) -> None:
        pass

    @abstractmethod
    def sede(self) -> None:
        pass

    @abstractmethod
    def estadio(self) -> None:
        pass

    @abstractmethod
    def presidente(self) -> None:
        pass


class Franquisia_CB(Franquisia_B):

    def __init__(self) -> None:
        self.nuevo()

    def nuevo(self) -> None:
        self._nuevaFranquisia = nuevaFranquisia1()

    @property
    def nuevaFranquisia(self) -> nuevaFranquisia1:
        nuevaFranquisia = self._nuevaFranquisia
        self.nuevo()
        return nuevaFranquisia

    def sede(self, img_sede) -> None:
        self._nuevaFranquisia.add("Fort Lauderdale,Florida")
        self.imagen_sede = img_sede

    def estadio(self, img_estadio) -> None:
        self._nuevaFranquisia.add("Lockhart Stadium")
        self.imagen_estadio = img_estadio

    def presidente(self, img_presidente) -> None:
        self._nuevaFranquisia.add("David Beckham")
        self.imagen_presidente = img_presidente

class nuevaFranquisia1():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Partes de la nueva franquisia en Miami: {', '.join(self.parts)}", end="")

class Mls:


    def __init__(self) -> None:
        self._Franquisia_B = None

    @property
    def Franquisia_B(self) -> Franquisia_B:
        return self._Franquisia_B

    @Franquisia_B.setter
    def Franquisia_B(self, Franquisia_B: Franquisia_B) -> None:
        self._Franquisia_B = Franquisia_B

    def Minimo_requerido_equipo(self, img_sede) -> None:
        self.Franquisia_B.sede(img_sede)

    def Puntos_requerido_equipo(self,img_sede,img_estadio, img_presidente) -> None:
        self.Franquisia_B.sede(img_sede)
        self.Franquisia_B.estadio(img_estadio)
        self.Franquisia_B.presidente(img_presidente)


if __name__ == "__main__":
    Mls = Mls()
    Franquisia_B = Franquisia_CB()
    Mls.Franquisia_B = Franquisia_B

    print("Cosa minima para tener un lugar en la liga: ")
    Mls.Minimo_requerido_equipo('./imagenes/builder/img_sede.jpg')
    Franquisia_B.nuevaFranquisia.list_parts()

    print("\n")

    print("Puntos para competir en la liga: ")
    Mls.Puntos_requerido_equipo('./imagenes/builder/img_sede.jpg', './imagenes/builder/img_estadio.jpg', './imagenes/builder/buil_2.jpg')
    Franquisia_B.nuevaFranquisia.list_parts()

    print("\n")

    # Remember, the Franquisia_B pattern can be used without a Mls class.
    print("Cosas de la nueva franquisia: ")
    Franquisia_B.sede('./imagenes/img_sede.jpg')
    Franquisia_B.estadio('./imagenes/img_estadio.jpg')
    Franquisia_B.presidente('./imagenes/buil_2.jpg')
    Franquisia_B.nuevaFranquisia.list_parts()

