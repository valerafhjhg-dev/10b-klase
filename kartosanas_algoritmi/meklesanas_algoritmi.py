#12/05/2026

#meklēšanas algoritmi

#Pārbaudām, vai dati eksistē
#kur tie atrodas
#Vai tekstā ir kāda noteikta daļa

vardi = ["Anna","Jānis","Pēteris"]

if "Anna" in vardi:
    print("Anna ir sarakstā")
else:
    print("Nav sarakstā")


#2. Meklēšana ar lietotājiem

vardi = ["Anna","Jānis","Pēteris"]
meklet = input("Ievadi vārdu, kuru vēlies meklēt: ")

if meklet in vardi:
    print("atrasts")
else:
    print("nav atrasts")

#3. Meklēšana csv failā 
meklet = input("Kādu vārdu meklēt?")
atrast = False


with open("datu apstrade un aprekini\klase.csv",encoding="utf-8") as f:
    next(f)

    for rinda in f:
        vards,atzimes = rinda.strip().split(",")

        if vards == meklet:
            print("atrasts")
            atrast = True
            break
    else:
        print("nav atrasts")

if not atrast:
    print("nav atrasts")


#4. Daļēja meklēšana

teksts = "programmēšana"

if "gram" in teksts:
    print("atrasts")
else:
    print("nav atrasts")
    