#27/01/2026

#python datu tips: Dictionary - vārdnīca/bibliootēka

#saraksts - []
#vārdnīca/bibliootēka - {}

#atslēgas: vērtība
#datu piekļušanai izmantojam atslēga

informacija = {"vārd":"Valerijs",
               "vecums": 16,
               "izglītība": "pamata"}

#8Izvadi izveidoto vārdnīcu
print(informacija)

#Izvadi vārdnīcas atslēgu
#Izvadi vārdnīcas atslēgu vertības

#Izmanto .keys() un .values()

print(informacija.keys())
print(informacija.values())


informacija["vecums"] = 17
print(informacija)

#izvadi tikai atslēgas vecums vērtību 
print(informacija["vecums"])


