import mysql.connector

def hae_lentokentat_maakoodilla(maakoodi):
    sql = f"SELECT tyyppi, maara FROM lentokentta WHERE country='{maakoodi}' GROUP BY tyyppi"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        print(f"Lentokenttien määrät maassa {maakoodi}:")
        for rivi in tulos:
            tyyppi = rivi[0]
            maara = rivi[1]
            print(f"{tyyppi}: {maara} kpl")
    return

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='lentokentat',
    user='localhost',
    password='',
    autocommit=True
)
maakoodi = input("Anna maakoodi (esim. FI): ")
hae_lentokentat_maakoodilla(maakoodi)
