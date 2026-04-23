#03.02.2026


#   Cikli - for
i = 1
for i in range(5):
   print(i)

#for ar sarakstu
   numbers = [3, 7, 2, 9]

for n in numbers:
    print(n * 2)

#for ar vārdnīcu(dictionary)


student = {
    "vārds": "Anna",
    "vecums": 16,
    "kurss": "Programmēšana"
}
for key, value in student.items():
    print(key, ":", value)
         
print(2%2)
print(7%2)
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "ir pāra skaitlis")

