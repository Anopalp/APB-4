def perbaruiTebakan(tebakan, jawaban, masukan):
    indexJawaban = jawaban.find(masukan)

    tebakanArr = list(tebakan)
    tebakanArr[indexJawaban] = masukan
    tebakan = "".join(tebakanArr)

    return tebakan