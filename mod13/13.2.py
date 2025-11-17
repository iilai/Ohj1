from flask import Flask
import mysql.connector
app = Flask(__name__)
yhteys = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="flight_game"
)
@app.route('/kenttä/<icao>')
def kentta(icao):
    sql = "SELECT ident, name, municipality FROM airport WHERE ident=%s"
    cursor = yhteys.cursor()
    cursor.execute(sql, (icao,))
    tulos = cursor.fetchone()
    return {
        "ICAO": tulos[0],
        "Name": tulos[1],
        "Municipality": tulos[2]
    }
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
