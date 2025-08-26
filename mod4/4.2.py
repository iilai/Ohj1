tuumat = float(input("Anna tuumien määrä ja anna negatiivinen numero, kun haluat lopettaa: "))
while tuumat>=0:
    sentit = tuumat * 2.54
    print(f"{tuumat} tuumaa = {sentit:.2f} cm")
    tuumat = float(input("Anna tuumien määrä ja anna negatiivinen numero, kun haluat lopettaa: "))

print("Ohjelma lopetettu.")