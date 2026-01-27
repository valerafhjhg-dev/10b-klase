#27/01/2026

"""Pajautā lietotājam:
vārdu (string)
vecumu (number)
trīs iecienītākās krāsas (list)
Saglabā datus vārdnīcā (dictionary)
Izvada visu informāciju vienā print() komandā"""

skolens = {}
skolens["vards"] = input("Ievadi vārdu: ")
skolens["vecums"] = int(input("Ievadi vecumu: "))
skolens["krasas"] = []
skolens["krasas"].append(input("Ievadi 1. iecienītāko krāsu: "))
skolens["krasas"].append(input("Ievadi 2. iecienītāko krāsu: "))
skolens["krasas"].append(input("Ievadi 3. iecienītāko krāsu: "))

print("Skolēna dati:", skolens)
