from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

class Sujeito(ABC):
    @abstractmethod
    def adicionar(self, observador: Observador) -> None:
        pass

    @abstractmethod
    def remover(self, observador: Observador) -> None:
        pass

    @abstractmethod
    def notificar(self) -> None:
        pass

class SujeitoConcreto(Sujeito):
    _estado: int = None
    _observadores: List[Observador] = []

    def adicionar(self, observador: Observador) -> None:
        print("SujeitoConcreto: Adicionando um observador.")
        self._observadores.append(observador)

    def remover(self, observador: Observador) -> None:
        self._observadores.remove(observador)

    def notificar(self) -> None:
        print("SujeitoConcreto: Notificando os observadores...")
        for observador in self._observadores:
            observador.atualizar(self)

    def executar_logica_principal(self) -> None:
        print("\nSujeitoConcreto: Estou fazendo algo importante.")
        self._estado = randrange(0, 10)

        print(f"SujeitoConcreto: Meu estado mudou para: {self._estado}")
        self.notificar()

class Observador(ABC):
    @abstractmethod
    def atualizar(self, sujeito: Sujeito) -> None:
        pass

class ObservadorConcretoA(Observador):
    def atualizar(self, sujeito: Sujeito) -> None:
        if isinstance(sujeito, SujeitoConcreto) and sujeito._estado >= 5:
            print("Observador A: Reagiu ao evento(Estado >= 5).")

class ObservadorConcretoB(Observador):
    def atualizar(self, sujeito: Sujeito) -> None:
        if isinstance(sujeito, SujeitoConcreto) and sujeito._estado <= 4:
            print("Observador B: Reagiu ao evento(Estado <= 4).")

# Código do cliente
if __name__ == "__main__":
    sujeito = SujeitoConcreto()

    observador_a = ObservadorConcretoA()
    sujeito.adicionar(observador_a)

    observador_b = ObservadorConcretoB()
    sujeito.adicionar(observador_b)

    sujeito.executar_logica_principal()
    sujeito.executar_logica_principal()

    sujeito.remover(observador_a)

    sujeito.executar_logica_principal()