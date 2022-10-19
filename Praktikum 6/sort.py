# Program Sort
# menerima N buah input bilangan yang disimpan di sebuah array.
# Lalu, implementasikan algoritma sorting, yaitu selection sort untuk mengurutkan
# bilangan dalam array tersebut dari besar ke kecil.
# Kemudian, print array yang telah diurutkan ke layar


# KAMUS
# array : array [0..N-1] of int
# i : int

# REALISASI FUNGSI DAN PROSEDUR
def get_max(arr, index_start):
    # mendapatkan maksimum array dari indeks indeks_start sampai selesai
    # KAMUS
    # Max, i : int
    # ALGORITMA
    Max = arr[index_start]
    for i in range(index_start+1, len(arr)):
        if arr[i] > Max:
            Max = arr[i]
    return Max

def get_idx(arr, number):
    # mendapatkan index dari suatu angka dalam array
    # KAMUS
    # i : int
    # ALGORITMA
    for i in range(len(arr)):
        if arr[i] == number:
            return i

def swap(array, indeks_1, indeks_2):
    # swap elemen array indeks 1 dengan indeks 2
    # KAMUS
    # ALGORITMA
    array[indeks_1], array[indeks_2] = array[indeks_2], array[indeks_1]

def sort(arr):
    for i in range(len(arr)):
        maxArr = get_max(arr, i)
        maxIdx = get_idx(arr, maxArr)
        swap(arr, i, maxIdx)
    print(arr)

# ALGORITMA PROGRAM UTAMA
array = []
for i in range(int(input())):
    array += [int(input())]
sort(array)