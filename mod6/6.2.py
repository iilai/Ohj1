import random
silmat = int(input("Kuinka monta tahkoa nopalla on? Heitän noppaa kunnes saan nopan maksimisilmäluvun. "))

def noppa():
    return random.randint(1,silmat)

while True:
    silmaluku=noppa()
    print(f"Silmänluku on: {silmaluku}.")
    if silmaluku == silmat:
        break