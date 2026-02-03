#03/02/2026

#cikls - while

count = 0

while count < 5:
    print(count)
    count = count + 1

#while ar lietotāja ievadi (string)
password = ""

while password != "1234":
    password = input("Ievadi paroli: ")

print("Pareiza parole!")

#break un continue
#📌 break – pārtrauc ciklu
for i in range(10):
    if i == 5:
        break
    print(i)