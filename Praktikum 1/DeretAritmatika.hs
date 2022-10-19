module DeretAritmatika where

-- DERET ARITMATIKA                     deretAritmatika(n,a,b)

-- DEFINISI DAN SPESIFIKASI
deretAritmatika :: Int -> Int -> Int -> Float
{- deretAritmatika(n,a,b) menghasilkan jumlah n suku pertama dari
   barisan aritmatika dengan parameter a merupakan suku pertama
   dari suatu barisan aritmatika yang memiliki beda b dengan n, a,
   dan b integer -}

-- REALISASI
deretAritmatika n a b = fromIntegral(n * (2 * a + (n-1) * b)) / 2