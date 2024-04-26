def perbaruiJawaban(tebakan, jawaban, masukan):
    indexJawaban = jawaban.find(masukan)

    jawabanArr = list(jawaban)
    jawabanArr[indexJawaban] = '-'
    jawaban = "".join(jawabanArr)

    return jawaban