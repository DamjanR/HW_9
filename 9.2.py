cifra = input("Izberi število med 1 in 100: ")
cifra = int(cifra)
print("Izbral si število: " + str(cifra))

print("")
i = 0
while i < cifra:
    i += 1
    print(i)
    if i == 3:
        print(i)
        print("Deljiv s 3 in 5")
else:
    print("Ni")
print("")
print("*** END ***")