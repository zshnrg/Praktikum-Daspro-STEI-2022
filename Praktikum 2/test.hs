module AlternateSort where
import Data.List

-- DEFINISI DAN SPESIFIKASI PREDIKAT
isEmpty :: [Int] -> Bool
-- isEmpty l  true jika list of Char l kosong
-- REALISASI
isEmpty l = null l

isOneElmt :: [Int] -> Bool
-- isOneElmt l true jika list of integer l hanya mempunyai satu elemen
-- REALISASI
isOneElmt l = (length l) == 1

-- DEFINISI DAN SPESIFIKASI KONSTRUKTOR
konso :: [Int] -> [Int] -> [Int]
{- konso l1 l2 menghasilkan sebuah list of integer dari li 
   (list of integer) dan li (list of integer)-}
-- REALISASI
konso l1 l2 = l1 ++ l2

-- =====================================================================
-- ALTERNATE SORT                                   alternateSort(li)

-- DEFINISI DAN SPESIFIKASI

gabungList :: [Int] -> [Int] -> [Int]
{- alternateSort(li) memiliki sebuah algoritma prosedural sebagai berikut.
   1. Urutkan list tersebut
   2. Bagi list menjadi 2 sama besar, misal l1 dan l2. Jika panjang list ganjil,
      maka l1 akan memiliki 1 elemen lebih banyak dibanding l2
   3. Ambil elemen terkecil dari l1, masukkan ke akhir l3.
   4. Ambil elemen terbesar dari l2, masukkan ke akhir l3.
   5. Ulangi langkah 3 dan 4 sampai kedua list kosong. -}

-- REALISASI
gabungList l1 l2 =
    if isEmpty l2 then if isEmpty l1 then [] else l1              -- basis
    else konso [head l1, last l2] (gabungList (tail l1) (init l2))  -- rekurens
