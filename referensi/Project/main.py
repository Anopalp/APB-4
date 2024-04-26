import os

from functions.cetakGambar import cetakGambar
from functions.apakahMenang import apakahMenang
from functions.apakahKalah import apakahKalah
from functions.apakahFormatSesuai import apakahFormatSesuai
from functions.apakahBenar import apakahBenar
from functions.inisialisasiTebakan import inisialisasiTebakan
from functions.perbaruiTebakan import perbaruiTebakan
from functions.perbaruiJawaban import perbaruiJawaban

clear = lambda: os.system('cls')

jawabanOri = "kucing"
jawabanDmy = jawabanOri
tebakan = inisialisasiTebakan(jawabanOri)
nyawa = 8

# Buat perulangan
while (not apakahMenang(jawabanOri, tebakan) and not apakahKalah(nyawa)):
    masukan = input("Masukkan tebakan: ")

    # Buat kondisional proses masukan
    if (apakahBenar(masukan, jawabanDmy)):
        print("\nTebakan benar!")
        # Buat prosedur setiap kondisional
        tebakan = perbaruiTebakan(tebakan, jawabanDmy, masukan)
        jawabanDmy = perbaruiJawaban(tebakan, jawabanDmy, masukan)
        cetakGambar(nyawa)
        print("Tebakan : " + tebakan + "\n")
    else:
        print("\nTebakan salah!")
        # Buat prosedur setiap kondisional
        nyawa -= 1
        cetakGambar(nyawa)
        print("Tebakan : " + tebakan + "\n")

if (nyawa == 0):
    print("Kamu kalah!")
else:
    print("Kamu menang!")

input("Press any key to close")
clear()
    