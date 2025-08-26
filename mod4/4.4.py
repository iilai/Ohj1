import random
luku = random.randint(1, 10)

while True:
    arvaus = int(input("Arvaa numero 1-10: "))

    if arvaus == luku:
        print("Oikein!")
        break
    elif arvaus < luku:
        print("Liian pieni arvaus")
    else:
        print("Liian suuri arvaus")