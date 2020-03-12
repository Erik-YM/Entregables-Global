from __future__ import annotations
from abc import ABC, abstractmethod


class Lavado:

    def __init__(self, Implementacion: Implementacion) -> None:
        self.Implementacion = Implementacion

    def aplicacion(self) -> str:
        return (f"Lavado Carroceria :\n"
                f"{self.Implementacion.aplicacion_Implementacion()}")


class LavadoCompleto(Lavado):

    def aplicacion(self) -> str:
        return (f"Lavado Completo: Incluye lavado de motor\n"
                f"{self.Implementacion.aplicacion_Implementacion()}")


class Implementacion(ABC):

    @abstractmethod
    def aplicacion_Implementacion(self) -> str:
        pass



class AutoUno(Implementacion):
    def aplicacion_Implementacion(self) -> str:
        return "Auto Uno: Asi lavaron este auto"


class AutoDos(Implementacion):
    def aplicacion_Implementacion(self) -> str:
        return "Auto Dos: Asi lavaron este auto."


def Cliente(lavado: Lavado) -> None:

    print(lavado.aplicacion(), end="")


if __name__ == "__main__":


    implementacion = AutoUno()
    lavado = Lavado(implementacion)
    Cliente(lavado)

    print("\n")

    implementacion = AutoDos()
    lavado = LavadoCompleto(implementacion)
    Cliente(lavado)
