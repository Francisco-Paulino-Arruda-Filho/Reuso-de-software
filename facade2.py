# Subsistema complexo
class CPU:
    def freeze(self):
        print("CPU: congelando processador...")

    def jump(self, position):
        print(f"CPU: saltando para a posição {position}...")

    def execute(self):
        print("CPU: executando instruções...")

class Memory:
    def load(self, position, data):
        print(f"Memória: carregando dados '{data}' na posição {position}...")

class HardDrive:
    def read(self, sector):
        print(f"Disco Rígido: lendo setor {sector}...")
        return f"dados do setor {sector}"

# Fachada que simplifica o uso do subsistema
class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start_computer(self):
        print("Iniciando o computador...")
        self.cpu.freeze()
        data = self.hard_drive.read("A1")
        self.memory.load("0x00", data)
        self.cpu.jump("0x00")
        self.cpu.execute()
        print("Computador iniciado com sucesso!")

# Cliente usa apenas a fachada
if __name__ == "__main__":
    computer = ComputerFacade()
    computer.start_computer()