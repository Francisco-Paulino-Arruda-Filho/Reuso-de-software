from pyparsing import ABC, abstractmethod
from typing import List

class Estrategia(ABC):
    @abstractmethod
    def executar_algoritmo(self, dados: List):
        pass

class Contexto:
    def __init__(self):
        pass

    @property
    def estrategia(self) -> Estrategia:
        return self._estrategia
    
    @estrategia.setter
    def estrategia(self, estrategia: Estrategia):
        self._estrategia = estrategia

    def executar_logica_de_negocio(self, dados: List) -> None:
        print("Ordenando dados usando a estratégia sem saber como ela faz isso.")
        resultado = self.estrategia.executar_algoritmo(dados)
        print(",".join(map(str, resultado)))
        print()  

class AlgoritmoConcretoA(Estrategia):
    def executar_algoritmo(self, dados: List):
        return sorted(dados)
    
class AlgoritmoConcretoB(Estrategia):
    def executar_algoritmo(self, dados: List):
        return list(reversed(sorted(dados)))
    
class Cliente:
    def __init__(self, estrategia: Estrategia):
        self.estrategia = estrategia
    
    def definir_estrategia(self, estrategia: Estrategia):
        self.estrategia = estrategia
    
    def executar(self, dados: List):
        return self.estrategia.executar_algoritmo(dados)
    
# Exemplo de uso
if __name__ == "__main__":
    dados = [5, 2, 9, 1, 5, 6]
    
    cliente = Cliente(AlgoritmoConcretoA())
    print("Usando AlgoritmoConcretoA:", cliente.executar(dados))
    
    cliente.definir_estrategia(AlgoritmoConcretoB())
    print("Usando AlgoritmoConcretoB:", cliente.executar(dados))