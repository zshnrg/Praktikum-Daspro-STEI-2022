module HitungIndeks where

-- HITUNG INDEX                         hitungIndeks(a,b,c)

-- DEFINISI DAN SPESIFIKASI
hitungIndeks :: Float -> Float -> Float -> Int
{- hitungIndeks(a,b,c) menerima 3 input bertipe float yaitu
   (berturut-turut) nilaiUTS, nilaiUAS, dan nilaiTubes. Fungsi
   akan mengeluarkan indeks mahasiswa (dinotasikan dengan
   bilangan bulat). Hanya ada 5 kemungkinan indeks dari seorang
   mahasiswa yaitu A, B, C, D, dan E. Setiap indeks dinotasikan
   dengan bilangan, A = 4, B = 3, dst sampai E = 0. -}

-- REALISASI
hitungIndeks a b c
    | a == 0 || b == 0 || c == 0 = 0
    | a < 40 || b < 40 = 1
    | c < 40 = 2
    | a < 75 && b < 75 && c < 75 = 2
    | a >= 75 && b >= 75 && c >= 75 = 4
    | otherwise = 3