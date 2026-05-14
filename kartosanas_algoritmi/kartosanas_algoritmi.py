#12/05/2026

#Kārtošanas algoritmi

#.sort() - metode

#sorted() - funkcija
 #1. skaitļu funkcija

skaitli = [5,9,3,20,2]

skaitli.sort(reverse=True)#Metode .sort() sakārto skaitļus dilstošā secībā

print(skaitli)

#3. vārdu sakārtošana

vardi = ["Anna","Jānis","Pēteris"]

vardi.sort()#Ja doti vārd, tie sakārtojas alfabētiskā secībā

print(vardi)

#4. Kārtošana no csv faila

with open("datu apstrade un aprekini\klase.csv",encoding="utf-8") as f:
    next(f) 
    for rinda in f:
        vards,atzimes = rinda.strip().split(",")
        atzimes.append(int(atzimes))

atzimes.capitalize
print(atzimes)
