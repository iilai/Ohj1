kuhan_pituus = float(input("Anna kuhan Pituus sentteinä: "))
kuhan_alimitta=37-kuhan_pituus
if kuhan_pituus < 37:
    print(f"Kuha on alimittainen {kuhan_alimitta:.2f} sentillä, joten kuha täytyy laskea takaisin järveen")
else:
    print("Kuha ei ole alimittainen, joten sitä ei tarvitse laskea takaisin järveen.")
