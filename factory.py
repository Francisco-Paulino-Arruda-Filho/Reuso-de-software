from __future__ import annotations
from abc import ABC, abstractmethod

class Criador(ABC):
    @abstractmethod
    def metodo_fabrica(self):
        pass

    def alguma_operacao(self) -> str:
        produto = self.metodo_fabrica()
        resultado = f"Criador: O mesmo código do criador funciona com {produto.operacao()}"
        return resultado
    
class Produto(ABC):
    @abstractmethod
    def operacao(self) -> str:
        pass

class ProdutoConcreto1(Produto):
    def operacao(self) -> str:
        return "{Resultado do ProdutoConcreto1}"
    
class ProdutoConcreto2(Produto):
    def operacao(self) -> str:
        return "{Resultado do ProdutoConcreto2}"
    
class CriadorConcreto1(Criador):
    def metodo_fabrica(self) -> Produto:
        return ProdutoConcreto1()
    
class CriadorConcreto2(Criador):
    def metodo_fabrica(self) -> Produto:
        return ProdutoConcreto2()
    
class Cliente:
    def __init__(self, criador: Criador) -> None:
        self.criador = criador
        
    def executar(self) -> None:
        print(f"Cliente: Eu nao sei a classe do criador, mas ainda assim funciona.\n"
              f"{self.criador.alguma_operacao()}")
        
# Exemplo de uso
if __name__ == "__main__":
    print("App: Iniciando o CriadorConcreto1.")
    cliente = Cliente(CriadorConcreto1())
    cliente.executar()
    
    print("\nApp: Iniciando o CriadorConcreto2.")
    cliente = Cliente(CriadorConcreto2())
    cliente.executar()