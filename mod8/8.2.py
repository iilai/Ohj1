import mysql.connector
def lentokenttienmaara(maakoodi):
    sql = f"SELECT kenttatyyppi FROM lentokentta WHERE maa='{maakoodi}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if kursori.rowcount > 0:
        maara = {}
        for rivi in tulos:
            tyyppi = rivi[0]
            if tyyppi in maara:
                maara[tyyppi] += 1
            else:
                maara[tyyppi] = 1

        print(f"\nMaassa {maakoodi} olevien lentokenttien lukumäärät tyypeittäin:")
        for tyyppi, lkm in maara.items():
            print(f"{tyyppi}: {lkm} kpl")
    else:
        print("Kyseisellä maakoodilla ei löytynyt lentokenttiä.")

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="",
    user="root",
    password="",
    autocommit=True
)

maakoodi = input("Anna maakoodi (esim. FI): ")
haelentokenttien_maarat(maakoodi)
