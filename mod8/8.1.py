import mysql.connector

def hae_lentokentta(icao):
    sql = f"SELECT name, city FROM airport WHERE ident='{icao}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentokentän nimi: {rivi[0]}, Sijaintikunta: {rivi[1]}")
    else:
        print("Lentokenttää ei löytynyt annetulla ICAO-koodilla.")
    return

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='lentokentta',
    user='localhost',
    password='',
    autocommit=True
)

icao = input("Anna ICAO-koodi: ")
hae_lentokentta(icao)
