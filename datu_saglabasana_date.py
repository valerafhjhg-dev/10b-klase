#05/05/2026

#Datu saglabāšana datnē

#Saglabāsim datus teksta failā
#Vienas rindas saglabāšana
with open("pirmais_fails.txt", "w", encoding="utf-8") as f: #w - write mode jeb rakstīšanas/izveidošana
    f.write("Sveika, Pasaule!")#.write() metode - ieraksta norādīto teksta failā
#Vairāku rindu saglabāšana
with open("otrais_fails.txt", "w", encoding="utf-8") as f: #r -  write mode jeb rakstīšanas/izveidošana
   f.write("Anna!")#.write() metode - ieraksta norādīto teksta failā 
   f.write("Pēteris!")

#Datu saglabāšana csv failā
with open("pirmais_csv_fails.csv","w",encoding="utf-8") as f:
    f.write("Vārds,Uzvārds,Vecums,Skola\n") #Pirmā rinda - kolonnu nosaukumi
    f.write("Anna,Bērziņa,17,Skola1\n") #Otrā rinda - pirmā datu rinda
#Datu pievenošana csv failā
with open("pirmais_csv_fails.csv","a",encoding="utf-8") as f: #a - append jeb pievienot
    f.write("Jānis,Ozoliņš,15,Rēzeknes valsts 1. ģimnāzija\n") 