#29/01/2026

#Nosacījumi: if, elif, else

vecums = int(input("Ievadi savu vecumu:")) #Datu ievade

#nosacījums
vecums = int(input("Ievadi savu vecumu: "))

if vecums >= 18:
    print("Tu esi pilngadīgs.")
else:
    print("Tu vēl neesi pilngadīgs.") #Izpildās ja nosacījumi nav
    
    
vards = input("Ievadi savu vārdu: ") #Ievade
#Nosacījums
if vards == "Anna": #Salīdzinot vērtības, jālieto ==
    print("Sveika, Anna!")
else:
    print("Sveiki, lietotāj!")


#Piemērs ar elif struktūru
    atzime = int(input("Ievadi atzīmi (1–10): ")) #Ievade

if atzime >= 9:
    print("Izcili!")
elif atzime >= 6:
    print("Ieskaite")
else:
    print("Nepietiekami")

#Saraksts
    augli = ["ābols", "banāns", "bumbieris"]

izvele = input("Ievadi augļa nosaukumu: ")

if izvele in augli:
    print("Šis auglis ir sarakstā.")

else:
    print("Šī augļa sarakstā nav.")

    
#Piemērs ar vārdnīcu
skolens = {
    "vards": "Jānis",
    "vecums": 16,
    "klase": "10.A"
}

if skolens["vecums"] >= 18:
    print("Skolēns ir pilngadīgs.")
else:
    print("Skolēns nav pilngadīgs.")



    #Nosacījumi ar vairākām pārbaudēm
    lietotajvards = input("Ievadi lietotājvārdu: ")
parole = input("Ievadi paroli: ")

#1.variants ar loģisko operatoru
if lietotajvards == "admins" and parole == "1234":
    print("Piekļuve atļauta.")
else:
    print("Nepareizs lietotājvārds vai parole.")