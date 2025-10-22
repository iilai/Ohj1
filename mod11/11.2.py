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

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottori(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensakapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensakapasiteetti = bensakapasiteetti

if __name__ == '__main__':
    sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
    polttoauto = Polttomoottori("ACD-123", 165, 32.3)

    sahkoauto.kiihdyta(90)
    polttoauto.kiihdyta(120)

    sahkoauto.kulje(3)
    polttoauto.kulje(3)

    print(f"Sähköauto: {sahkoauto.kuljettu_matka} km")
    print(f"Polttomoottoriauto: {polttoauto.kuljettu_matka} km")