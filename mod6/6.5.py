def parittomatpois(numerolista):
    parilliset = []
    for luku in numerolista:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset

def paaohjelma():
    lista = [1,2,3,4,5,6,7,8,9,10]
    vainparilliset =  parittomatpois(lista)
    print(f"Lista parittomien kanssa {lista}.")
    print(f"Lista, jossa vain parilliset {vainparilliset}.")
paaohjelma()
