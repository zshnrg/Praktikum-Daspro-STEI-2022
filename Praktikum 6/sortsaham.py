# Program SortSaham
# Spesifikasi: Membaca data kepemilikan saham sebuah perusahaan dari suatu file teks
#              dan mengurutkan data tersebut ke layar berdasarkan IdPemilik secara
#              terurut membesar serta menuliskan kembali data tersebut dalam keadaan terurut ke layar.

import tulisdata

# KAMUS
# type dataSaham  : <IdPemilik : string, { Kode Pemilik Saham }
#                    IdPT : string,      { Kode Perusahaan }
#                    Nilai : integer>    { Nilai saham, dalam juta rupiah }
# namafile: string

def lenn(arr):
    length = 0
    for e in arr:
        length += 1
    return length

def BacaDataSaham(namafile):
    # Membaca file nama file data kepemililikan saham
    # KAMUS
    # f : file teks
    # row  array of str
    # dataSaham = array of dataSaham
    # i : int
    # ALGORITMA
    f = open(namafile, "r")
    row = f.readlines()
    dataSaham = []
    i = 0
    while row[i] != "99999999":
        dataSaham += [[row[i], row[i+1], row[i+2]]]
        i += 3
    return dataSaham

def sort(dataSaham):
    # Mengurutkan data saham dengan algoritma sorting insertion sort
    # KAMUS
    # ALGORITMA
    for Pass in range(1, lenn(dataSaham)):
        Temp = dataSaham[Pass]
        i = Pass-1
        while Temp[0] < dataSaham[i][0] and i > 0:
            dataSaham[i+1] = dataSaham[i]
            i -= 1
        if Temp[0] >= dataSaham[i][0]:
            dataSaham[i+1] = Temp
        else:
            dataSaham[i+1] = dataSaham[i]
            dataSaham[i] = Temp
    printDataSaham(dataSaham)
    
def printDataSaham(dataSaham):
    for i in range(lenn(dataSaham)):
        for j in range(3):
            elemen = ''
            for k in range(lenn(dataSaham[i][j])-1):
                if dataSaham[i][j][k] + dataSaham[i][j][k+1] != '\\n':
                    elemen += dataSaham[i][j][k]
            print(elemen, end='')
            if j != 2: print(',', end='')
        print()


# ALGORITMA PROGRAM UTAMA
namafile = input()
tulisdata.TulisDataSaham(namafile)
dataSaham = BacaDataSaham(namafile)
if dataSaham != []:
    sort(dataSaham)
else:
    print('File kosong')