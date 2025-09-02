import math
def yksikkohintalasku(halkaisija, hinta):
    ala = halkaisija / 100 / 2 ** 2 * math.pi
    yksikkohinta = hinta/ala
    return yksikkohinta

def paaohjelma():
    print("Ensimmäisen pitsan tiedot: ")
    halkaisija1 = float(input("Halkaisija 1 (cm): "))
    hinta1 = float(input("Hinta 1 (€): "))

    print("Toisen pitsan tiedot: ")
    halkaisija2 = float(input("Halkaisija 2 (cm): "))
    hinta2 = float(input("Hinta 2 (€)"))

    yksikkohinta1 = yksikkohintalasku(halkaisija1, hinta1)
    yksikkohinta2 = yksikkohintalasku(halkaisija2, hinta2)

    print(f"Pitsan 1 yksikköhinta on {yksikkohinta1:.2f} €/m^2.")
    print(f"Pitsan 2 yksikköhinta on {yksikkohinta2:.2f} €/m^2.")

    if yksikkohinta1 > yksikkohinta2:
        print("Pizzalla 2 on alhaisempi yksikköhinta")
    elif yksikkohinta1 < yksikkohinta2:
        print("Pizzalla 1 on alhaisempi yksikköhinta")
    else:
        print("Pizzoilla on sama yksikköhinta!")
paaohjelma()

