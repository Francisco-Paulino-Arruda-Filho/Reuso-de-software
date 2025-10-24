from __future__ import annotations
from abc import ABC, abstractmethod

class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass

class SimpleCommand(Command):
    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: Executando com o payload ({self._payload})")

class Receiver:
    def do_something(self, a: str) -> None:
        print(f"Receiver: Trabalhando em ({a}.)")

    def do_something_else(self, b: str) -> None:
        print(f"Receiver: Tambem trabalhando em ({b}.)")

class ComplexCommand(Command):
    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        print("ComplexCommand: Iniciando uma operacao complexa.")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)

class Invoker:
    _on_start: Command = None
    _on_finish: Command = None

    def set_on_start(self, command: Command) -> None:
        self._on_start = command

    def set_on_finish(self, command: Command) -> None:
        self._on_finish = command

    def do_something_important(self) -> None:
        print("Invoker: Esta prestes a iniciar algo importante...")

        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...fazendo algo realmente importante...")

        print("Invoker: Esta prestes a finalizar algo importante...")

        if isinstance(self._on_finish, Command):
            self._on_finish.execute()

def client_code() -> None:
    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Say Hi!"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(receiver, "Send email", "Save report"))
    invoker.do_something_important()


if __name__ == "__main__":    
    client_code()