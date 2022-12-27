module HitungIndeks where

-- HITUNG INDEX                         hitungIndeks(a,b,c)

-- DEFINISI DAN SPESIFIKASI
hitungIndeks :: Float -> Float -> Float -> Int
{- hitungIndeks(a,b,c) menerima 3 input bertipe float yaitu
   (berturut-turut) nilaiUTS, nilaiUAS, dan nilaiTubes. Fungsi
   akan mengeluarkan indeks mahasiswa (dinotasikan dengan
   bilangan bulat). Hanya ada 5 kemungkinan indeks dari seorang
   mahasiswa yaitu A, B, C, D, dan E. Setiap indeks dinotasikan
   dengan bilangan, A = 4, B = 3, dst sampai E = 0.
   - Apabila setiap nilai (3 nilai) lebih dari sama dengan 75, maka mendapat indeks A
   - Apabila hanya 1 atau 2 nilai yang lebih dari sama dengan 75, maka mendapat indeks B
   - Apabila nilai tubes yang di bawah 40, tapi uts dan uas di atas 40 (biarpun di atas 75 sekalipun) maka mendapat indeks C
   - Apabila semua nilai di bawah 75 dan tidak ada yang di bawah 40, maka juga mendapat indeks C
   - Apabila nilai uts atau uas di bawah 40, maka mendapat indeks D tidak peduli nilai tubes
   - Apabila ada satu nilai yang 0, maka indeks otomatis E -}

-- REALISASI
hitungIndeks a b c
    | a == 0 || b == 0 || c == 0 = 0
    | a < 40 || b < 40 = 1
    | c < 40 = 2
    | a < 75 && b < 75 && c < 75 = 2
    | a >= 75 && b >= 75 && c >= 75 = 4
    | otherwise = 3