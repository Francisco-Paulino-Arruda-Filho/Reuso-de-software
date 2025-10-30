from abc import ABC, abstractmethod
from typing import Any

# Interface de Estado
class State(ABC):
    @abstractmethod
    def handle(self, context):
        pass

# Contexto
class Document:
    def __init__(self):
        self.state = DraftState()

    def set_state(self, state: Any):
        self.state = state

    def publish(self):
        self.state.handle(self)

# Estados concretos
class DraftState(State):
    def handle(self, context):
        print("Enviando documento para moderação...")
        context.set_state(ModerationState())

class ModerationState(State):
    def handle(self, context):
        print("Publicando documento aprovado...")
        context.set_state(PublishedState())

class PublishedState(State):
    def handle(self, context):
        print("Documento já está publicado.")

def codigo_cliente():
    document = Document()
    document.publish()  # Do rascunho para moderação
    document.publish()  # Da moderação para publicado
    document.publish()  # Já está publicado

if __name__ == "__main__":
    codigo_cliente()