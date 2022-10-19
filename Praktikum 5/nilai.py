# Program: Nilai
#

# KAMUS

# ALGORITMA
nilai = int(input())

if nilai == -9999: print('Data nilai kosong')
else:
    count_mhs = 0
    count_lulus = 0
    count_tidaklulus = 0
    Sum = 0
    while (nilai != -9999):
        if 0 <= nilai <= 100:
            count_mhs += 1
            Sum += nilai
            if nilai >= 40: count_lulus += 1
            else: count_tidaklulus += 1
        nilai = int(input())
    print(count_mhs)
    if (count_mhs != 0):
        print(count_lulus)
        print(count_tidaklulus)
        print('{:.02f}'.format(Sum / count_mhs))