nimia = set()
kysyttynimi=0

while True:
    if kysyttynimi =="":
        break
    else:
        kysyttynimi=input("Anna nimi tai syötä tyhjä merkkikenttä lopettaaksesi: ")
        if kysyttynimi not in nimia:
            print("Uusi nimi.")
            nimia.add(kysyttynimi)
        else:
            print("Aiemmin syötetty nimi.")

print("\nNimet: ")
for n in nimia:
    print(n)