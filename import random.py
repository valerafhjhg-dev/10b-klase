import random 
print("Ļaipni ludzam mezs gemerators")

# jautajuma lietom 
n = int(input("ciik daudz koku iestadi"))

#zimejuma koku rimndu]\
for i in range(n):
    print("%", end="") # izvedam koku emoji

    print() # parejajs uz jauno rinu 

    # zem kokiem paradas nejausi objekti
    for i in range(n):
        obj = random.choice(["🌎","🌎","🌎"])
        print(obj, end="") #izvejda, izveleto obj\

        print()  #parejam uz jauno rindu
        print("-" * 40)
        #motevejosha uz jauno rindu 
        fraze = random.choice([
            "esi  lieal smalxis "
            "parak domnats"
            "parakakaka"
        ])

        print(fraze)
        print("tu esi popka un tu esi parak daudz malcis")