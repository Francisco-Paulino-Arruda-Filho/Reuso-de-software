class Componente:
    def operacao(self) -> str:
        pass


class ComponenteConcreto(Componente):
    def operacao(self) -> str:
        return "ComponenteConcreto"


class Decorador(Componente):
    def __init__(self, componente: Componente) -> None:
        self._componente = componente

    def operacao(self) -> str:
        return self._componente.operacao()


class DecoradorConcretoA(Decorador):
    def operacao(self) -> str:
        return f"DecoradorConcretoA({self._componente.operacao()})"


class DecoradorConcretoB(Decorador):
    def operacao(self) -> str:
        return f"DecoradorConcretoB({self._componente.operacao()})"


# Código cliente
if __name__ == "__main__":
    componente_simples = ComponenteConcreto()
    print("Cliente: Componente simples:")
    print(componente_simples.operacao())

    decorador1 = DecoradorConcretoA(componente_simples)
    decorador2 = DecoradorConcretoB(decorador1)
    print("\nCliente: Componente decorado:")
    print(decorador2.operacao())
