import random
def noppa():
    return random.randint(1,6)

while True:
    silmaluku=noppa()
    print(f"Silmänluku on: {silmaluku}.")
    if silmaluku == 6:
        break