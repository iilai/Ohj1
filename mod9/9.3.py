class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.tamanhetkinen_nopeus += muutos
        if self.tamanhetkinen_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        elif self.tamanhetkinen_nopeus < 0:
            self.tamanhetkinen_nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.tamanhetkinen_nopeus * tunnit


def main():
    auto = Auto("ABC-123", 142)

    auto.kiihdyta(30)
    auto.kiihdyta(70)
    auto.kiihdyta(50)
    print(f"Auton tämänhetkinen nopeus: {auto.tamanhetkinen_nopeus}.")

    auto.kiihdyta(-200)
    print(f"Auton tämänhetkinen nopeus: {auto.tamanhetkinen_nopeus}.")

    print(f"Auton rekisteritunnus: {auto.rekisteritunnus}.")
    print(f"Auton huippunopeus: {auto.huippunopeus}km/h.")
    print(f"Auton tämänhetkinen nopeus: {auto.tamanhetkinen_nopeus}km/h.")
    print(f"Kuljettu matka: {auto.kuljettu_matka}km.")

    auto.kiihdyta(60)
    auto.kuljettu_matka = 2000
    auto.kulje(1.5)

    print(f"Kuljettu matka : {auto.kuljettu_matka}km.")

if __name__ == "__main__":
    main()