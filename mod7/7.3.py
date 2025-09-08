lentoasematiedot = {}

while True:
    vastaus=input("Haluatko syöttää uuden lentoaseman, hakea vai lopettaa ohjelman (uusi/hakea/lopettaa): ")
    if vastaus=="lopettaa":
        break
    elif vastaus=="uusi":
        icao=input("Anna lentoaseman ICAO-koodi: ")
        lentoasema=input("Anna lentoaseman nimi: ")
        lentoasematiedot[icao]=lentoasema
        print("Lentoasema syötetty.")
    elif vastaus=="hakea":
        icao=input("Anna lentoaseman icao: ")
        if icao in lentoasematiedot:
            print("Lentoasematiedot",lentoasematiedot[icao])
        else:
            print("Lentoasemtietoja ei löydy.")
    else:
        print("Ohjelma lopetettu.")

