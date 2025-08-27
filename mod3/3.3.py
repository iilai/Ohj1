sukupuoli = input("Anna biologinen sukupuoli (N tai M): ")

hemoglobiini = float(input("Anna hemoglobiiniarvosi (g/l) ilman yksikköä: "))

sukupuoli = sukupuoli.upper()

if sukupuoli == "N" and (117<=hemoglobiini<=175):
    print("Hemoglobiiniarvosi ovat normaalit.")
elif sukupuoli == "N" and (hemoglobiini>175):
    print("Hemoglobiiniarvosi ovat korkeat.")
elif sukupuoli == "N" and (hemoglobiini<117):
    print("Hemoglobiiniarvosi ovat matalat.")

if sukupuoli == "M" and (134<=hemoglobiini<=195):
    print("Hemoglobiiniarvosi ovat normaalit.")
elif sukupuoli == "M" and (hemoglobiini>195):
    print("Hemoglobiiniarvosi ovat korkeat.")
elif sukupuoli == "M" and (hemoglobiini<134):
    print("Hemoglobiiniarvosi ovat matalat.")

else:
    print("Syötä sukupuoleksi joko N tai M")
