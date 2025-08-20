leiviska= input("Anna leiviskät: ")
naula= input("Anna naulat: ")
luoti= input("Anna luodit: ")

luotip=13.3
naulap=float(luotip)*32
leiviskap=float(naulap)*20

paino = float(luotip)*float(luoti)+float(leiviskap)*float(leiviska)+float(naulap)*float(naula)
kilot = float(paino)//1000
grammat = float(paino)%1000
print(f"Massa nykymittojen mukaan: {kilot} kilogrammaa ja {grammat:.2f} grammaa")

