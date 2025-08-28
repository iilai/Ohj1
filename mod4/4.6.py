import random

N = int(input("Kuinka monta pistettä arvotaan? "))

kerrat = 0
ympyrassan = 0
while kerrat < N:
    if random.uniform(-1,1)**2 + random.uniform(-1,1)**2 < 1:
        ympyrassan += 1
    kerrat += 1

print("π =", 4 * ympyrassan / N)
