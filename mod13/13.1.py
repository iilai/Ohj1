from flask import Flask
app = Flask(__name__)
def tarkista_alkuluku(n):
    if n <= 1:
        return False
    alkuluku = True
    for x in range(2, n-1):
        if n % x == 0:
            alkuluku = False
            break
    return alkuluku

@app.route('/alkuluku/<int:luku>')
def alkuluku(luku):
    return {
        "Number": luku,
        "isPrime": tarkista_alkuluku(luku)
    }

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
