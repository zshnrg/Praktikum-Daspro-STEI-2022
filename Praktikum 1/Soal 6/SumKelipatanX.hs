module SumKelipatanX where

-- KELIPATAN X                                  sumKelipatanX(m.n.x)

-- DEFINISI DAN SPESIFIKASI
sumKelipatanX :: Int -> Int -> Int -> Int
{- menerima masukan dua buah integer positif (integer > 0), misalnya
   m dan n, serta sebuah integer positif lain, yaitu x, dan
   menghasilkan jumlah bilangan kelipatan x di antara m dan n (m
   dan n termasuk) dengan menggunakan ekspresi rekursif yang basisnya
   m = n -}

-- REALISASI
sumKelipatanX m n x
    | m == n = if mod m x == 0 then m else 0
    | otherwise =
        if mod m x == 0 then m + sumKelipatanX (m+1) n x
        else sumKelipatanX (m+1) n x
        