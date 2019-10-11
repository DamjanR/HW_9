import random

skrito_stevilo = random.randint(1, 100)

with open("tocke.txt") as datoteka:
    stari_stevec = int(datoteka.read())

print("Prejšno število poskusov je bilo: " + str(stari_stevec))

stevec = 0
while True:
    vneseno_število = int(input("Ugani število: "))
    stevec += 1

    if vneseno_število == skrito_stevilo:
        print("Ugnili ste pravo stevilo")
        break
    elif vneseno_število > skrito_stevilo:
        print("Vpisali se preveliko število")
    else:
        print("Vpisali ste premalo število")

print("Število poskusov je bilo: " + str(stevec))

if stevec < stari_stevec:
    with open("tocke.txt", "w") as datoteka:
        datoteka.write(str(stevec))

print("Konec programa")