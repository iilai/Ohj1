import requests
import json

hakusana = input("Anna paikkakunnan nimi, niin annan säätilan ja lämpötilan celsius asteina: ")

apiavain = "apiavain"

pyynto = f"https://api.openweathermap.org/data/2.5/weather?q={hakusana}&appid={apiavain}&units=metric&lang=fi"

vastaus = requests.get(pyynto).json()

if vastaus['cod'] == 200:
    print(f"Sää paikassa {vastaus['name']}: {vastaus['weather'][0]['description']}")
    print(f"Lämpötila: {vastaus['main']['temp']} celsius astetta.")
else:
    print("Haku ei onnistunut.")
