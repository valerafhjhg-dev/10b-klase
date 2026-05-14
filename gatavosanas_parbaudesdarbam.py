#14/05/2026

#Gatavošanās pārbaudes darbam

#1 uzdevums

#1.1. Nosaki, kuri dati ir kvalitatīvi. Pamato.

#Laura, 17, Rīga: Kvalitatīvs
#???, -15, Mēness: Nav kvalitatīvs
#Jānis, 18: Nav kvalitatīvs

#1.2. Pārveido dotos nestrukturētos datus strukturētā tabulā.

#“Marta dzīvo Jelgavā un viņai ir 16 gadi.”

#Marta, Jelgava, 16

#2. uzdevums

#2.1. Uzraksti programmu, kas pārbauda, vai ievadītais skaitlis ir robežās no 1 līdz 10.

#skaitlis=int(input("Ievadi skaitli no 1 līdz 10: "))
#if 0 <= skaitlis <= 10:
#    print("Skaitlis ir no 1 līdz 10.")  
#else:
#    print("Skaitlis nav no 1 līdz 10.")

#2.2. Paskaidro, kāpēc validācija ir svarīga programmās.

#jo tā pārbauda datus

#3. uzdevums — Datu apstrāde CSV failā
#Dota datne:

 
#produkts,cena
#Piens,1.50
#Maize,2.00
#Sula,3.20
#Cepumi,4.50
 

with open("produkti_fails.txt", "w", encoding="utf-8") as f:
    f.write("Sveika, Pasaule!")

with open("otrais_fails.txt", "w", encoding="utf-8") as f:
   f.write("Piens") 
   f.write("Maize")
   f.write("Sula")
   f.write("Cepumi")
   
with open("produkti_csv_fails.csv","w",encoding="utf-8") as f:
    f.write("Produkts,Cena\n")
    f.write("Piens,1.50\n")
    f.write("Maize,2.00\n")
    f.write("Sula,3.20\n")
    f.write("Cepumi,4.50\n")

#3.1.Uzraksti programmu, kas izvada tikai produktus, kuru cena ir lielāka par 2.00.
with open("produkti_csv_fails.csv", "r", encoding="utf-8") as f:
    next(f)

    for rinda in f:
        produkts, cena = rinda.strip().split(",")

        if float(cena) > 2.00:
            print(produkts, cena)

#3.2.Aprēķini visu produktu kopējo summu.

#4uzdevums — Kārtošana

#4.1. Sakārto sarakstu dilstošā secībā

scores = [7, 10, 5, 8, 9]