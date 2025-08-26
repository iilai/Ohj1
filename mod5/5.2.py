luvut = []
while True:
    numero = (input("Anna luku: "))
    if numero == "":
        break
    luku = float(numero)
    luvut.append(luku)
    luvut.sort(reverse=True)
print(f"Neljä suurinta lukua olivat {luvut[0:5]}.")