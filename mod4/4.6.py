import random

N = int(input("Kuinka monta pistettä arvotaan? "))

kerrat = 0
ympyrassa = 0
while kerrat < N:
    if random.uniform(-1,1)**2 + random.uniform(-1,1)**2 < 1:
        ympyrassa += 1
    kerrat += 1

print("Arvio π ≈", 4 * ympyrassa / N)