# Program RataSiswa
# membaca data siswa dari suatu tempat kursus dari suatu file teks dan menuliskan nilai rata-rata setiap siswa ke layar.
# Nilai rata-rata ditampilkan terurut berdasarkan NoInduk siswa.

import tulisdata

# KAMUS
# type dataSiswa  : <NoInduk: string, KodeKursus : string, Nilai : integer>
# namafile : str

def lenn(arr):
    length = 0
    for e in arr:
        length += 1
    return length

def BacaDataSiswa(namafile):
    # Membaca file nama file data kepemililikan Siswa
    # KAMUS
    # f : file teks
    # row  array of str
    # dataSiswa = array of dataSiswa
    # i : int
    # ALGORITMA
    f = open(namafile, "r")
    row = f.readlines()
    dataSiswa = []
    i = 0
    while row[i] != "99999999":
        dataSiswa += [[row[i], row[i+1], row[i+2]]]
        i += 3
    return dataSiswa

def sort(dataSiswa):
    # Mengurutkan data Siswa dengan algoritma sorting insertion sort
    # KAMUS
    # ALGORITMA
    for Pass in range(1, lenn(dataSiswa)):
        Temp = dataSiswa[Pass]
        i = Pass-1
        while Temp[0] < dataSiswa[i][0] and i > 0:
            dataSiswa[i+1] = dataSiswa[i]
            i -= 1
        if Temp[0] >= dataSiswa[i][0]:
            dataSiswa[i+1] = Temp
        else:
            dataSiswa[i+1] = dataSiswa[i]
            dataSiswa[i] = Temp
    printDataSiswa(dataSiswa)

def printDataSiswa(dataSiswa):
    for i in range(lenn(dataSiswa)):
        for j in range(3):
            elemen = ''
            for k in range(lenn(dataSiswa[i][j])-1):
                if dataSiswa[i][j][k] + dataSiswa[i][j][k+1] != '\\n':
                    elemen += dataSiswa[i][j][k]
            print(elemen, end='')
            if j != 2: print(',', end='')
        print()

# ALGORITMA PROGRAM UTAMA
namafile = input()
tulisdata.TulisDataSiswa(namafile)
dataSiswa = BacaDataSiswa(namafile)
if dataSiswa != []:
    sort(dataSiswa)
else:
    print('File kosong')