#19/05/2026

with open("dati_ieskaite.txt", "w", encoding="utf-8") as f:
    f.write("Sveika, Pasaule!")

with open("dati_ieskaite.txt", "w", encoding="utf-8") as f:
   f.write("Anna") 
   f.write("Jānis")
   f.write("Laura")
   f.write("Marta")
   
with open("dati_ieskaite.csv","w",encoding="utf-8") as f:
    f.write("Vārds,vecums\n")
    f.write("Anna,16\n")
    f.write("Jānis,18\n")
    f.write("Laura,20\n")
    f.write("Marta,15\n")
