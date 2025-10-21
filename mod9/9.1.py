class Auto:

    def __init__(self, rekisteritunnus, huippunopeus, kiihdyta):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0
        self.kiihdyta = 0

def main():
    auto = Auto("ABC-123", 142)

    print(f"Auton rekisteritunnus: {auto.rekisteritunnus}.")
    print(f"Auton huippunopeus: {auto.huippunopeus}km/h.")
    print(f"Auton tämänhetkinen nopeus: {auto.tamanhetkinen_nopeus}km/h.")
    print(f"Kuljettu matka: {auto.kuljettu_matka}km.")

if __name__ == "__main__":
    main()