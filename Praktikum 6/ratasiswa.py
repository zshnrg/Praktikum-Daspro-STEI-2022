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

def sort(data):
    for Pass in range(1, lenn(data)):
        Temp = data[Pass]
        i = Pass - 1
        while i >= 0 and int(Temp[0]) < int(data[i][0]):
            data[i+1] = data[i]
            i -= 1
        data[i+1] = Temp

def Cetak(data):
    for i in range(lenn(data)):
        for j in range(8):
            print(data[i][0][j], end='')
        print('=' + "{:.02f}".format(data[i][1]/data[i][2]))

# ALGORITMA PROGRAM UTAMA
namafile = input()
tulisdata.TulisDataSiswa(namafile)

f = open(namafile, "r")
line1 = f.readline()
if line1 != "99999999":
    list_sum_nilai = []

    while line1 != "99999999":
        line2 = f.readline()
        line3 = f.readline()

        found = False
        for i in range(lenn(list_sum_nilai)):
            if line1 == list_sum_nilai[i][0]:
                found = True; idx = i
        
        if found:
            list_sum_nilai[idx][1] += int(line3)
            list_sum_nilai[idx][2] += 1
        else:
            list_sum_nilai += [[line1, int(line3), 1]]
        
        line1 = f.readline()

    sort(list_sum_nilai)
    Cetak(list_sum_nilai)
        

else:
    print('File kosong')