while True:
    kayttajatunnus = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")
    if kayttajatunnus != "python" or salasana != "rules":
        print("Pääsy evätty. Kokeile uudestaan.")
    else:
        print("Tervetuloa!")
        break
