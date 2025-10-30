# Produto
class Car:
    def __init__(self):
        self.seats = 0
        self.engine = ""
        self.gps = False

# Interface Builder
class Builder:
    def set_seats(self, num):
        pass
    def set_engine(self, type):
        pass
    def set_gps(self, enabled):
        pass
    def get_result(self):
        pass

# Builder concreto
class CarBuilder(Builder):
    def __init__(self):
        self.car = Car()

    def set_seats(self, num):
        self.car.seats = num

    def set_engine(self, type):
        self.car.engine = type

    def set_gps(self, enabled):
        self.car.gps = enabled

    def get_result(self):
        return self.car

# Diretor
class Director:
    def construct_sports_car(self, builder):
        builder.set_seats(2)
        builder.set_engine("V8")
        builder.set_gps(True)

# Cliente
if __name__ == "__main__":
    builder = CarBuilder()
    director = Director()
    director.construct_sports_car(builder)
    car = builder.get_result()
    print(f"Carro esportivo: motor {car.engine}, {car.seats} lugares, GPS={car.gps}")