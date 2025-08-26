kokonaisluku = int(input(" Anna kokonaisluku ja ratkaisen onko se alkuluku: "))
if kokonaisluku <= 1:
    print("Ei ole alkuluku.")
else:
    alkuluku = True
    for x in range(2, kokonaisluku-1):
        if kokonaisluku % x == 0:
            alkuluku = False
            break
    if alkuluku:
         print("On alkuluku.")
    else:
        print("Ei ole alkuluku.")

