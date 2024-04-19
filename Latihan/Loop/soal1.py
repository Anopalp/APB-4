jawaban = "jeruk"
clue = "Buah yang berwarna oranye dan rasanya asam-manis\n"

print("\nClue: " + clue)
tebakan = input("Tebak buah : ")

while (tebakan != jawaban):
    print("\nTebakan salah!\n")
    tebakan = input("Tebak buah : ")

print("\nTebakan benar!\n")