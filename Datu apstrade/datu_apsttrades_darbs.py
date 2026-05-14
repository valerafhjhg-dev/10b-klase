#05/05/2026


#📝 Uzdevums 1
#Izvada tikai skolēnus ar atzīmi < 7

#📝 Uzdevums 2
#Aprēķini augstāko atzīmi

#📝 Uzdevums 3
#Saskaiti, cik skolēniem atzīme ≥ 8

#📝 Uzdevums 4
#Izveido programmu, kas:

#izvada skolēnus virs vidējās atzīmes

#1. uzdevums
with open("datu apstrade_un_aprekini.py",encoding="utf-8") as f:
    next(f) 
    for rinda in f:
        vards,atzīme = rinda.strip().split(",")
        if int(atzīme) < 7:
                print(vards)

#2. uzdevums
with open("datu apstrade_un_aprekini.py",encoding="utf-8") as f:
    next(f) 
    for rinda in f:
        vards,atzīme = rinda.strip().split(",")
        if int(atzīme) > lielakaATZIME
        