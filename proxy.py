from abc import ABC, abstractmethod 

class Assunto(ABC):
    @abstractmethod
    def requisicao(self) -> str:
        pass

class AssuntoReal(Assunto):
    def requisicao(self) -> str:
        print("AssuntoReal: Processando a requisição.")

class Proxy(Assunto):
    def __init__(self, assunto: Assunto):
        self._assunto = assunto

    def requisicao(self) -> str:
        if self.verificar_acesso():
            self._assunto.requisicao()
            self.registrar_acesso()

    def verificar_acesso(self) -> None:
        print("Proxy: Verificando acesso antes de encaminhar a requisicao.")

    def registrar_acesso(self) -> None:
        print("Proxy: Registrando o acesso após a requisicao.")

def client_code(assunto: Assunto) -> None:
    assunto.requisicao()

if __name__ == "__main__":
    assunto_real = AssuntoReal()
    proxy = Proxy(assunto_real)
    client_code(proxy)