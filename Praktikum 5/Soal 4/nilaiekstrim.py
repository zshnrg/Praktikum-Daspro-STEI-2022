# Program NilaiEkstrim
# membaca sebuah integer N (asumsikan 0 < N <= 100).
# membaca N buah integer dan menyimpan setiap integer ke dalam suatu array.
# Selanjutnya, program menerima masukan sebuah nilai integer, misalnya X, dan menampilkan:
# - Jika X ada di array, apakah X adalah nilai maksimum (tuliskan “maksimum”) ataunilai minimum
#   (tuliskan “minimum”) atau keduanya. Jika bukan nilai maksimum atau minimum, menuliskan “N#A”.
# - Jika X tidak ada di array, tuliskan “X tidak ada”. 

# KAMUS
# N, X : int
# Num : array [0..N-1] of int
# maxNum, minNum : int
# ada : bool

# ALGORITMA
N = int(input())
Num = [0 for i in range(N)]

for i in range(N): Num[i] = int(input())

X = int(input())

maxNum = Num[0]
minNum = Num[0]

for i in range(N):
    if Num[i] > maxNum: maxNum = Num[i]
    if Num[i] < minNum: minNum = Num[i]

ada = False
for i in range(N):
    if X == Num[i]: ada = True

if ada:
    if X == maxNum: print('maksimum')
    if X == minNum: print('minimum')
    if X != maxNum and X != minNum: print('N#A')
else: print(X, 'tidak ada')