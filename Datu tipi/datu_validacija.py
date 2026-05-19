#23/04/2026

#Datu validacija

#Datu ievade
vards = input("Ievadi vārdu: ")
print(vards)

if vards.isalpha(): #.isalpha()metode pārbauda, vai saņemtais lielums ir burti vai nav
    print ("Ir burti")
else:
    print("Nav burti")

    print("Tu esi pilngadīgs.")#Izpildās, ja nosacījums ir patiess
else:
    print("Tu vēl neesi pilngadīgs.")#Izpildās, ja nosacījums nav patiess
else:
    print("Nav skaitlis")
