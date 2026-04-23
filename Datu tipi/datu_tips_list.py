#22/01/2026

#List - saraksts

#saraksts var saturēt vairākas vērtības un arī dažādus datu tipus

#izveidojam sarakstu un pieškiram vētības
masinas = ["Audi", "BMW", "Opel", "VW"] 
#teksts, vesel skaitlis, decimālskaitlis, saraksts
saraksts1 = ["anna", 5,4.2, [1,2,3]]

masinas = ["Audi", "BMW", "Opel", "VW", "Mercedes"]
print(masinas)
#izvadi pirmo un pēdejo elementu
#ideksēšana
print(masinas[0])
print(masinas[-1])

#pieveinot jaunu elementu
#.append() - mwetode 
masinas.append("Toyota")
print(masinas)

#nomaini vienu esošu elementu
masinas[1] = "Ferrari"
print(masinas)
