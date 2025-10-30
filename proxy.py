from abc import ABC, abstractmethod 
import time

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


# Interface comum
class YouTubeService(ABC):
    @abstractmethod
    def get_video(self, video_id: str) -> str:
        pass

class YouTubeAPI(YouTubeService):
    def get_video(self, video_id: str) -> str:
        print(f"Baixando vídeo '{video_id}' do YouTube...")
        time.sleep(2) 
        return f"Conteúdo do vídeo {video_id}"

class CachedYouTubeProxy(YouTubeService):
    def __init__(self, real_service: YouTubeService):
        self._real_service = real_service
        self._cache = {}

    def get_video(self, video_id: str) -> str:
        if video_id not in self._cache:
            print("Cache ausente. Chamando o serviço real...")
            self._cache[video_id] = self._real_service.get_video(video_id)
        else:
            print("Retornando vídeo do cache.")
        return self._cache[video_id]

if __name__ == "__main__":
    service = YouTubeAPI()
    proxy = CachedYouTubeProxy(service)

    print(proxy.get_video("abc123")) 
    print(proxy.get_video("abc123")) 



if __name__ == "__main__":
    assunto_real = AssuntoReal()
    proxy = Proxy(assunto_real)
    client_code(proxy)