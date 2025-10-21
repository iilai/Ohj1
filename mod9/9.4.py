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


def main():
    autot = []
    for i in range(10):
        huippunopeus = random.randint(100, 200)
        autot.append(Auto(f"ABC-{i+1}", huippunopeus))  # luodaan Auto-olio

    kilpailu = True
    while kilpailu:
        for auto in autot:
            muutos = random.randint(-10, 15)
            auto.kiihdyta(muutos)
            auto.kulje(1)
            if auto.kuljettu_matka >= 10000:
                kilpailu = False
                break

    print(f"{'Rekisteri':<15}{'Huippunopeus':<15}{'Nopeus':<15}{'Matka':<15}")
    for auto in autot:
        print(f"{auto.rekisteritunnus:<15}{auto.huippunopeus:<15}"
              f"{auto.tamanhetkinen_nopeus:<15}{auto.kuljettu_matka:<15}")


if __name__ == "__main__":
    main()