class Alvo:
    def requisicao(self):
        return "Resultado da requisicao do Alvo"

class Adpter:
    def requisicao_especifica(self):
        alvo = Alvo()
        return f"Adaptacao: (TRANSLATED) {alvo.requisicao()}"
    
class Adaptador(Alvo, Adpter):
    def requisicao(self):
        return self.requisicao_especifica()
    
def codigo_cliente(alvo: Alvo) -> None:
    print(alvo.requisicao(), end="")

if __name__ == "__main__":
    print("Cliente: Eu posso trabalhar com Alvo:")
    alvo = Alvo()
    codigo_cliente(alvo)
    print("\n")
    
    adaptador = Adaptador()
    print("Cliente: Agora eu posso trabalhar com o Adaptador:")
    codigo_cliente(adaptador)
    print()