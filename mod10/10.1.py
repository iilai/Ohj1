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
        while self.nykyinen_kerros < haluttu_kerros:
            self.kerros_ylos()
        while self.nykyinen_kerros > haluttu_kerros:
            self.kerros_alas()

def main():
    h = Hissi(0, 10)
    h.siirry_kerrokseen(5)
    h.siirry_kerrokseen(2)
    h.siirry_kerrokseen(4)
    h.siirry_kerrokseen(1)

if __name__ == "__main__":
    main()
