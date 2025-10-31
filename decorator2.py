# Interface base
class Notifier:
    def send(self, message):
        pass

# Componente concreto
class EmailNotifier(Notifier):
    def send(self, message):
        print(f"Enviando e-mail: {message}")

# Decorador base
class NotifierDecorator(Notifier):
    def __init__(self, notifier):
        self._notifier = notifier

    def send(self, message):
        self._notifier.send(message)

# Decoradores concretos
class SMSNotifier(NotifierDecorator):
    def send(self, message):
        super().send(message)
        print(f"Enviando SMS: {message}")

class SlackNotifier(NotifierDecorator):
    def send(self, message):
        super().send(message)
        print(f"Enviando mensagem no Slack: {message}")

# Uso
notifier = SlackNotifier(SMSNotifier(EmailNotifier()))
notifier.send("Servidor fora do ar!")

def client_code():
    notifier = SlackNotifier(SMSNotifier(EmailNotifier()))
    notifier.send("Alerta: Uso elevado de CPU!")

if __name__ == "__main__":
    client_code()