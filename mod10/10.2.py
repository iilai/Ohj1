class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on kerroksessa {self.nykyinen_kerros}.")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on kerroksessa {self.nykyinen_kerros}.")

    def siirry_kerrokseen(self, haluttu_kerros):
        print(f"Hissi on aloituskerroksessa {self.nykyinen_kerros}.")
        while self.nykyinen_kerros < haluttu_kerros:
            self.kerros_ylos()
        while self.nykyinen_kerros > haluttu_kerros:
            self.kerros_alas()

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.hissit = []
        for i in range(hissien_lkm):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))
        self.alin_kerros = alin_kerros

    def aja_hissia(self, hissin_numero, kohdekerros):
        if 0 <= hissin_numero < 3:
            print(f"Käytetään hissiä {hissin_numero + 1}.")
            hissi = self.hissit[hissin_numero]
            hissi.siirry_kerrokseen(kohdekerros)

def main():
    talo = Talo(1,10,3)
    talo.aja_hissia(0, 5)
    talo.aja_hissia(1, 8)
    talo.aja_hissia(2, 2)
    talo.aja_hissia(1, 2)


if __name__ == "__main__":
    main()
