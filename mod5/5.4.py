kaupungit = []
for i in range(5):
    kaupunki = input(f"Anna kaupungin {i+1} nimi: ")
    kaupungit.append(kaupunki)
print("Kaupungit:")
for i in kaupungit:
    print(i)