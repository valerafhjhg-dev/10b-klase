#05/05/2026

#datu apstrāde un aprēķini

#Nolasīt un izvadīt datus

with open("klase.csv",encoding="utf-8") as f:
    next(f) 
    for rinda in f:
        vards,atzīme = rinda.strip().split(",")
        print(vards,atzīme)

with open("klase.csv",encoding="utf-8") as f:
    next(f) 
    for rinda in f:
        vards,atzīme = rinda.strip().split(",")
        if int(atzīme) >= 8:
                print(vards):

with open("klase.csv",encoding="utf-8") as f:
    next(f) 
    for rinda in f:
        vards,atzīme = rinda.strip().split(",")
        summa+=int(atzīme)

print(summa)

summa = 0
skaits = 0
with open("klase.csv",encoding="utf-8") as f:
    next(f) 
    for rinda in f:
        vards,atzīme = rinda.strip().split(",")
        summa+=int(atzīme)
        skaits+=1