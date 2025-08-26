syote = input("Anna luku: ")

if syote == "":
    print("Et antanut yhtään lukua.")
else:
    luku = float(syote)
    pienin = luku
    suurin = luku

    while True:
        syote = input("Anna luku: ")
        if syote == "":
            break

        luku = float(syote)
        if luku < pienin:
            pienin = luku
        if luku > suurin:
            suurin = luku

    print("Pienin:", pienin)
    print("Suurin:", suurin)