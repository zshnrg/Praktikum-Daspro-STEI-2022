module Max3 where

-- MAX3                                             max3(a,b,c)

-- DEFINISI DAN SPESIFIKASI
max3 :: Int -> Int -> Int -> Int
{- max3 (a,b,c) mengirimkan nilai yang paling besar di antara a,
   b, dan c. Asumsi: a, b, c bilangan berbeda -}

-- REALISASI
max3 a b c
    | a > b && a > c = a
    | b > a && b > c = b
    | otherwise = c