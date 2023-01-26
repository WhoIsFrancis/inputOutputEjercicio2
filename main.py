import pickle

class Vehiculo:
    ruedas = 0
    puertas = 0
    motor = ""

    def __init__(self, ruedas, puertas, motor):
        self.ruedas = ruedas
        self.puertas = puertas
        self.motor = motor

    def __str__(self):
        return f"Es un vehiculo de {self.ruedas} ruedas, con {self.puertas} puertas y de motor {self.motor}"


auto1 = Vehiculo(4, 5, "Diesel")

f = open("vehiculo.bin", "wb")
pickle.dump(auto1, f)
f.close()

f = open("vehiculo.bin", "rb")
auto = pickle.load(f)
print(auto)


