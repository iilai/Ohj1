import random

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


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdyta(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"{'Rekisteri':<15}{'Huippunopeus':<15}{'Nopeus':<15}{'Matka':<15}")
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<15}{auto.huippunopeus:<15}"
                  f"{auto.tamanhetkinen_nopeus:<15}{auto.kuljettu_matka:<15}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False


def main():
    autot = []
    for i in range(10):
        huippunopeus = random.randint(100, 200)
        autot.append(Auto(f"ABC-{i+1}", huippunopeus))

    romuralli = Kilpailu("Suuri romuralli", 8000, autot)

    tunnit = 0
    while not romuralli.kilpailu_ohi():
        romuralli.tunti_kuluu()
        tunnit += 1
        if tunnit % 10 == 0:
            print(f"Tilanne {tunnit} tunnin jälkeen:")
            romuralli.tulosta_tilanne()

    print(f"Kilpailu päättyi {tunnit} tunnin jälkeen!")
    romuralli.tulosta_tilanne()


if __name__ == "__main__":
    main()
