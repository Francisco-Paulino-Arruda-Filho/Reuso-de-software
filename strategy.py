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

class Criptografia(ABC):
    @abstractmethod
    def criptografar(self, texto: str) -> str:
        pass

class CriptografiaSimples(Criptografia):
    def criptografar(self, texto: str) -> str:
        return ''.join(chr(ord(c) + 1) for c in texto)
    
class CifragemCesar(Criptografia):
    def criptografar(self, texto: str) -> str:
        deslocamento = 3
        resultado = ""
        for char in texto:
            if char.isalpha():
                deslocado = chr((ord(char) - 65 + deslocamento) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + deslocamento) % 26 + 97)
                resultado += deslocado
            else:
                resultado += char
        return resultado
    
class CifragemSubstituicao(Criptografia):
    def criptografar(self, texto: str) -> str:
        tabela_substituicao = str.maketrans("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba")
        return texto.translate(tabela_substituicao)
    
class CifragemVinigere(Criptografia):
    def criptografar(self, texto: str) -> str:
        chave = "KEY"
        resultado = []
        chave_repetida = (chave * (len(texto) // len(chave) + 1))[:len(texto)]
        for t_char, k_char in zip(texto, chave_repetida):
            if t_char.isalpha():
                deslocamento = ord(k_char.upper()) - ord('A')
                base = ord('A') if t_char.isupper() else ord('a')
                resultado.append(chr((ord(t_char) - base + deslocamento) % 26 + base))
            else:
                resultado.append(t_char)
        return ''.join(resultado)

def cliente_criptografia(criptografia: Criptografia, texto: str) -> str:
    return criptografia.criptografar(texto)

if __name__ == "__main__":
    texto = "Hello, World!"
    
    criptografia_simples = CriptografiaSimples()
    print("Criptografia Simples:", cliente_criptografia(criptografia_simples, texto))
    
    cifragem_cesar = CifragemCesar()
    print("Cifragem de César:", cliente_criptografia(cifragem_cesar, texto))
    
    cifragem_substituicao = CifragemSubstituicao()
    print("Cifragem por Substituição:", cliente_criptografia(cifragem_substituicao, texto))
    
    cifragem_vinigere = CifragemVinigere()
    print("Cifragem de Vinigere:", cliente_criptografia(cifragem_vinigere, texto))