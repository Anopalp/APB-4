import os, time

def isValidPilgan(jawaban):
    kunci = ['A', 'a', 'B', 'b']
    lenKunci = len(kunci)
    retVal = False
    for i in range(lenKunci):
        if (jawaban == kunci[i]):
            retVal = True
    return retVal

def isTrue(jawaban, kunci, tipeSoal):
    if (tipeSoal == "Isian"):
        return (jawaban == kunci)
    else:
        return (jawaban.lower() == kunci)

clear = lambda: os.system('cls')

soal = [{"soal": "17"                                                                   , "jawaban": 'a', "tipe": "tdPG"},
        {"soal": "17.0"                                                                 , "jawaban": 'b', "tipe": "tdPG"},
        {"soal": "SMAN 11 BANDUNG"                                                      , "jawaban": 'd', "tipe": "tdPG"},
        {"soal": "\';\'"                                                                , "jawaban": 'c', "tipe": "tdPG"},
        {"soal": "\'1\'"                                                                , "jawaban": 'c', "tipe": "tdPG"},
        {"soal": "\"123\""                                                              , "jawaban": 'd', "tipe": "tdPG"},
        {"soal": "True"                                                                 , "jawaban": 'e', "tipe": "tdPG"},
        {"soal": "\"False\""                                                            , "jawaban": 'd', "tipe": "tdPG"},
        {"soal": "a = 17 % 3\nprint(a)"                                                 , "jawaban": '2', "tipe": "Isian"},
        {"soal": "a = 30\nb = 12\nc = 30 * 12\nb = 3\nc = 9\nprint(c)"                  , "jawaban": '9', "tipe": "Isian"},
        {"soal": "a = \"Aku\"\nb = \"Pasti\"\nc = \"Bisa\"\nprint(a + b + c)"           , "jawaban": 'AkuPastiBisa', "tipe": "Isian"},
        {"soal": "a = \"KitaBisa\"\nb = \"kitabisa\"\nc = (a == b)\nprint(c)"           , "jawaban": 'b', "tipe": "boolPG"},
        {"soal": "a = \"KitaBisa\"\nb = \"KitaBisa\"\nc = not (a != b)\nprint(c)"       , "jawaban": 'a', "tipe": "boolPG"},
        {"soal": "suhuKamar = 25\nsuhuPanas = suhuKamar > 30\nprint(suhuPanas)"         , "jawaban": 'b', "tipe": "boolPG"},
        {"soal": "a = 1 != \"1\"\nprint(a)"                                             , "jawaban": 'b', "tipe": "boolPG"},
        {"soal": "a = 8 - 4\nb = 4\nc = a > b\nprint(c)"                                , "jawaban": 'b', "tipe": "boolPG"},
        {"soal": "a = 83 > 22\nb = 30 >= 31\nc = a and b\nprint(c)"                     , "jawaban": 'b', "tipe": "boolPG"},
        {"soal": "z = (1 != 1) and (100 > 0)\nprint(z)"                                 , "jawaban": 'b', "tipe": "boolPG"},
        {"soal": "umur = 16\nremaja = (umur > 12) and (umur >= 0)\nprint(remaja)"       , "jawaban": 'a', "tipe": "boolPG"},
        {"soal": "kkm = 70\nnilaiAnda = 80\nlulus = (nilaiAnda - kkm) > 0\nprint(lulus)", "jawaban": 'a', "tipe": "boolPG"}
        ]

# INISIALISASI QUIZ
input("Press any key to begin")
clear()

start_time = time.time()

for i in range(len(soal)):
    if (soal[i]['tipe'] == 'tdPG'):
        print(f"Apa tipe data dari\n\n{soal[i]['soal']}\n")
        print("a. Integer\nb. Float / Double\nc. Char\nd. String\ne. Boolean\n")
    else:
        print(f"Apa hasil output (print) dari program ini\n\n{soal[i]['soal']}\n")
        if (soal[i]['tipe'] == 'boolPG'):
            print("a. True\nb. False\n")
    jawaban = input("JAWABAN : ")
    while (not isTrue(jawaban, soal[i]['jawaban'], soal[i]['tipe'])):
        clear()
        if ((soal[i]['tipe'] == "boolPG") and (not isValidPilgan(jawaban))):
            print("Masukan Anda salah. Pilih \"a\" atau \"b\"!\n")
        elif ((soal[i]['tipe'] == "tdPG") and (not isValidPilgan(jawaban))):
            print("Masukan Anda salah. Pilih \"a\", \"b\", \"c\", \"d\", atau \"e\"!\n")
        else:
            print("Jawaban Salah! Masukkan jawaban lagi!\n")
        if (soal[i]['tipe'] == 'tdPG'):
            print(f"Apa tipe data dari\n\n{soal[i]['soal']}\n")
            print("a. Integer\nb. Float / Double\nc. Char\nd. String\ne. Boolean\n")
        else:
            print(f"Apa hasil output (print) dari program ini\n\n{soal[i]['soal']}\n")
            if (soal[i]['tipe'] == 'boolPG'):
                print("a. True\nb. False\n")
        jawaban = input("JAWABAN : ")
    print("BENAR!\n")
    input("Press button to continue")
    clear()

end_time = time.time()

print(f'Execution time : {end_time-start_time} seconds')