#12/05/2026

#Mājasdarbs

#CSV faila izveide ar5 produktu un to cenu
with open("datu apstrade\produkti.csv","w",encoding="utf-8") as f:
    f.write("Maize,2\n")
    f.write("Piens,1.2\n")
    f.write("siers,5.6\n")
    f.write("Kūka,12.4\n")
    f.write("Saldējums,0.68\n")

#Aprēkina kopējo summu

with open("datu apstrade\produkti.csv",encoding="utf-8") as f:
    summa =0 
    lielakacena = 0

    for rinda in f:
        produkts,cena = rinda.strip().split(",")
        summa+=float(cena)
        if float(cena) > lielakacena:
            lielakacena = float(cena)
