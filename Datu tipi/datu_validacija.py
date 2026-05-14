#23/04/2026

#Datu validacija

#Datu ievade
vecums = input("Ievadi vecumu: ")
print(vecums)

if vecums.isdigit(): #.isdigit()metode pārbauda, vai saņemtais lielums ir skaitlis vai nav
    print ("Ir skaitlis")
    if int (vecums) >=18: 
        print("Tu esi pilngadīgs.")#Izpildās, ja nosacījums ir patiess
    else:
        print("Tu vēl neesi pilngadīgs.")#Izpildās, ja nosacījums nav patiess
else:
    print("Nav skaitlis")



