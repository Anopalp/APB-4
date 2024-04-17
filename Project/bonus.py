from functions.cetakGambar import cetakGambar
from functions.apakahMenang import apakahMenang
from functions.apakahKalah import apakahKalah
from functions.apakahFormatSesuai import apakahFormatSesuai
from functions.apakahBenar import apakahBenar
from functions.inisialisasiTebakan import inisialisasiTebakan
from functions.perbaruiTebakan import perbaruiTebakan
from functions.perbaruiJawaban import perbaruiJawaban

jawabanOri = "kucing"
jawabanDmy = jawabanOri
tebakan = inisialisasiTebakan(jawabanOri)
nyawa = 8

while (not apakahMenang(jawabanOri, tebakan) and not apakahKalah(nyawa)):
    masukan = input("Masukkan tebakan: ")

    while (not apakahFormatSesuai(masukan)):
        print("\nFormat tebakan salah!\n")
        masukan = input("Masukkan tebakan: ")

    if (apakahBenar(masukan, jawabanDmy)):
        print("\nTebakan benar!")
        tebakan = perbaruiTebakan(tebakan, jawabanDmy, masukan)
        jawabanDmy = perbaruiJawaban(tebakan, jawabanDmy, masukan)
        cetakGambar(nyawa)
        print("Tebakan : " + tebakan + "\n")
    else:
        print("\nTebakan salah!")
        nyawa -= 1
        cetakGambar(nyawa)
        print("Tebakan : " + tebakan + "\n")

if (nyawa == 0):
    print("Kamu kalah!")
else:
    print("Kamu menang!")
    