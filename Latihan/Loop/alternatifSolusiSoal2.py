jawaban = "jeruk"
clue = "Buah yang berwarna oranye dan rasanya asam-manis\n"
nyawa = 3

print("\nNyawa : " + str(nyawa))
print("Clue: " + clue)

tebakan = input("Tebak buah : ")

if (tebakan != jawaban):
    nyawa -= 1

while ((tebakan != jawaban) and (nyawa > 0)):
    print("\nTebakan salah!\n")
    print("Nyawa tersisa : " + str(nyawa))
    tebakan = input("Tebak buah : ")
    if (tebakan != jawaban):
        nyawa -= 1

print("\nGame selesai!")

print("Nyawa : " + str(nyawa))