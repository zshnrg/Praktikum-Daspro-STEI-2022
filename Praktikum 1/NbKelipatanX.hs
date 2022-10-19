module NbKelipatanX where

-- KELIPATAN X                                  nbKelipatanX(m.n.x)

-- DEFINISI DAN SPESIFIKASI
nbKelipatanX :: Int -> Int -> Int -> Int
{- menerima masukan dua buah integer positif (integer > 0), misalnya
   m dan n, serta sebuah integer positif lain, yaitu x, dan
   menghasilkan banyaknya bilangan kelipatan x di antara m dan n (m
   dan n termasuk) dengan menggunakan ekspresi rekursif yang basisnya
   m = n -}

-- REALISASI
nbKelipatanX m n x
    | m == n = if mod m x == 0 then 1 else 0
    | otherwise =
        if mod m x == 0 then 1 + nbKelipatanX (m+1) n x
        else 0 + nbKelipatanX (m+1) n x
        