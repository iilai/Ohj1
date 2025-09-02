def gallonitlitroiksi(gallonit):
    return gallonit * 3.785

def paaohjelma():
    while True:
        gallon = float(input("Gallonit: "))
        if gallon < 0:
            print("Negatiivinen arvo.")
            break
        litrat = gallonitlitroiksi(gallon)
        print(f"{gallon} gallonaa on {litrat:.3f} litraa.")

paaohjelma()