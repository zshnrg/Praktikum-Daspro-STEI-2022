-- DEFINISI DAN SPESIFIKASI PREDIKAT
isEmpty :: [Int] -> Bool
-- isEmpty l  true jika list of Char l kosong
-- REALISASI
isEmpty l = null l

-- ====================================================================
-- NBOCC                                            nbOcc(l,x)

-- DEFINISI DAN SPESIFIKASI
nbOcc :: [Int] -> Int -> Int
{- Menghasilkan berapa banyak kemunculan x pada list integer l -}

-- REALISASI
nbOcc l x =
    if isEmpty l then 0                 -- basis
    else if head l == x then 1 + nbOcc (tail l) x       -- rekurens
    else nbOcc (tail l) x                               -- rekurens
