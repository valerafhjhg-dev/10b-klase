#05.02.2026

#Funkcijas

"""
Funkcijas pamatstruktūra
def funkcijas_nosauums (paramertri):
     # darbības
     return rezultāts
def - atslēgvārds funkcijas izveidei
parametri - dati, ko funkcija saņem
return - vērtība, ko funkcija atgriež (nav obligāta)
"""

#Piemērs ar skaitļiem (number)
#Funkcija, kas aprēķina dievu skaitļu summu
def summa(a,b):
    return a + b

rezultats = summa(1,2)
print(rezultats)

#Piemērs ar tekstu (string)
#Funkcija, kas izvada sveicienu
def sveiciens(vards):
    return "Sveiks, " + vards + "!"
print(sveiciens("Anna"))

#Piemērs ar sarakstu (list)
#Funkcija, kas saskaita elementu sarakstā
def elementu_skaits(saraksts):
    skaits = 0
    for elemets in saraksts:
        skaits += 1
        return skaits
print(elementu_skaits("6"))


#Piemērs ar vārdnīcu (dictionary)
#Funkcija, kas pārbauda, vai vārdnīva ir noteikta atslēga 
def vai_ir_atslēga(dati,atslēga):
    if atslēga in dati:
        return "atslēga ir atrasta"
    else:
        return "Atslēga nav atrasta"
    studenti = {
        "vārds": "Jānis",
        "vecums": 16
    }
    print(vai_ir_atslēga(studenti, "skola"))