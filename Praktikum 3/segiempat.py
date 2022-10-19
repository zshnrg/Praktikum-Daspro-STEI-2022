# Program: Segi Empat

# KAMUS
# N : int
# C1 : string
# C2 : string
# i, j : int

# ALGORITMA
N = int(input())
C1 = str(input())[0]
C2 = str(input())[0]

if N > 0 and (C1 != C2):
    for i in range(N):
        for j in range(N):
            if i == 0 or i == N-1:
                print(C1, end='')
            elif j == 0 or j == N-1:
                print(C1, end='')
            else:
                print(C2, end='')
        print()
else:
    print('Masukan tidak valid')
