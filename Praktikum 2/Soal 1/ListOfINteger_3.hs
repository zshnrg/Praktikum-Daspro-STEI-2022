-- DEFINISI DAN SPESIFIKASI PREDIKAT
isOneElmt :: [Int] -> Bool
-- isOneElmt l true jika list of integer l hanya mempunyai satu elemen
-- REALISASI
isOneElmt l = (length l) == 1

-- ====================================================================
-- ELEMEN KE N LIST                             elmtKeN(l, n)

-- DEFINISI DAN SPESIFIKASI
elmtKeN :: [Int] -> Int -> Int
{- Menghasilkan berapa banyak kemunculan x pada list integer l -}

-- REALISASI
elmtKeN l n =
    if n == 1 then head l                 -- basis
    else elmtKeN (tail l) (n - 1)         -- rekurens
