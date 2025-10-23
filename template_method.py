from abc import ABC, abstractmethod

class ClasseAbstrata(ABC):
    def template_method(self) -> None:
        self.operacao_base1()
        self.operacoes_requeridas1()
        self.operacao_base2()
        self.operacoes_requeridas2()

    def operacao_base1(self) -> None:
        print("ClasseAbstrata: Estou fazendo a maior parte do trabalho")

    def operacao_base2(self) -> None:
        print("ClasseAbstrata: Mas permito que subclasses substituam algumas operacoes")

    def operacao_base3(self) -> None:
        print("ClasseAbstrata: Ainda assim faco maior parte do trabalho")

    @abstractmethod
    def operacoes_requeridas1(self) -> None:
        pass

    @abstractmethod
    def operacoes_requeridas2(self) -> None:
        pass

    def gancho1(self) -> None:
        pass

    def gancho2(self) -> None:
        pass

class ClasseConcreta1(ClasseAbstrata):
    
    def operacoes_requeridas1(self):
        print("Classe concreta 1: Operacao 1 implementada")

    def operacoes_requeridas2(self):
        print("Classe concreta 1: Operacao 2 implementada")

class ClasseConcreta2(ClasseAbstrata):
    
    def operacoes_requeridas1(self):
        print("Classe concreta 2: Operacao 1 implementada")

    def operacoes_requeridas2(self):
        print("Classe concreta 2: Operacao 2 implementada")

    def gancho1(self):
        print("Classe concreta 2: Gancho 1 sobrescrito")

def codigo_cliente(classe_abstrata: ClasseAbstrata) -> None:
    classe_abstrata.template_method()

if __name__ == "__main__":
    codigo_cliente(ClasseConcreta1())

    codigo_cliente(ClasseConcreta2())
