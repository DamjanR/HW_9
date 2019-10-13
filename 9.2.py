cifra = input("Izberi število med 1 in 100: ")
cifra = int(cifra)
print("Izbral si število: " + str(cifra))

print("")
i = 0
while i < cifra:
    i += 1
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

print("")
print("*** END ***")