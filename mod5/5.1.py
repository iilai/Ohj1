import random
arvottu = []
summa = 0
arpakuutiot = int(input("Anna arpakuutioiden lukumäärä: "))
for i in range(arpakuutiot):
    silmaluku = (random.randint(1,6))
    arvottu.append(silmaluku)
    summa += silmaluku
print(f"Heitot: {arvottu}")
print(f"Arpakuutioiden silmälukujen summa on {summa}.")


