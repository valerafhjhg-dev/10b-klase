#19/05/2026

vards = input("Ievadi vārdu: ")
print(vards)

if vards.startswith(vards[0].upper()):
    print("Vārds sākas ar lielo burtu.")
else:
    print("Vārds nav sākts ar lielo burtu.")