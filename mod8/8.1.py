import mysql.connector

def haelentokentta(icao):
    sql = f"SELECT nimi, sijaintikunta FROM lentokentta WHERE ident='{icao}'"
    print(sql)

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if len(tulos) > 0:
        for rivi in tulos:
            print(f"Lentoasema: {rivi[0]}, sijaintikunta: {rivi[1]}")
    else:
        print("ICAO-koodilla ei ole lentokenttää.")

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="lentokentta",
    user="root",
    password="",
    autocommit=True
)

icao = input("Anna lentoaseman icao: ")
haelentokentta(icao)
