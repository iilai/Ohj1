def laskesumma(lista):
    summa = 0
    for luku in lista:
        summa += luku
    return summa

def paaohjelma():
    numerot = [1, 2, 3, 4, 5]
    tulos = laskesumma(numerot)
    print(f"Listan {numerot} summa on {tulos}")

paaohjelma()