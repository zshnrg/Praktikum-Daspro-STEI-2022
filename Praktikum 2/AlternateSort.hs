module AlternateSort where

-- DEFINISI DAN SPESIFIKASI LIST
{- type List of Int: [ ] atau [e o List] atau [List o e]  
   Definisi type List of Int
   Basis: List of Int kosong adalah list of Int 
   Rekurens: 
   List tidak kosong dibuat dengan menambahkan sebuah elemen bertype Int di awal 
   sebuah list atau
   dibuat dengan menambahkan sebuah elemen bertype Int di akhir sebuah list -}

-- DEFINISI DAN SPESIFIKASI KONSTRUKTOR
konso :: Int -> [Int] -> [Int]
{- konso e li menghasilkan sebuah list of integer dari li 
   (list of integer) dan li (list of integer)-}
-- REALISASI
konso e li = [e] ++ li

konsoList :: [Int] -> [Int] -> [Int]
{- konso li1 li2 menghasilkan sebuah list of integer dari li 
   (list of integer) dan li (list of integer)-}
-- REALISASI
konsoList li1 li2 = li1 ++ li2

-- DEFINISI DAN SPESIFIKASI SELEKTOR
-- head :: [Int] -> Int
-- head l menghasilkan elemen pertama list l, l tidak kosong

-- tail :: [Int] -> [Int]
-- tail l menghasilkan list tanpa elemen pertama list l, l tidak kosong

-- last :: [Int] -> Int
-- last l menghasilkan elemen terakhir list l, l tidak kosong

-- init :: [Int] -> [Int]
-- init l menghasilkan list tanpa elemen terakhir list l, l tidak kosong

-- DEFINISI DAN SPESIFIKASI PREDIKAT
isEmpty :: [Int] -> Bool
-- isEmpty l  true jika list of Char l kosong
-- REALISASI
isEmpty l = null l

isOneElmt :: [Int] -> Bool
-- isOneElmt l true jika list of integer l hanya mempunyai satu elemen
-- REALISASI
isOneElmt l = (length l) == 1

-- DEFINISI DAN SPESIFIKASI MODUL DATA LIST
-- sort :: [Int] -> [Int]
-- sort mengurutkan elemen list dari yang terkecil ke terbesar

-- =====================================================================
-- ALTERNATE SORT                                   alternateSort(li)

-- DEFINISI DAN SPESIFIKASI

alternateSort :: [Int] -> [Int]
{- alternateSort(li) memiliki sebuah algoritma prosedural sebagai berikut.
   1. Urutkan list tersebut
   2. Bagi list menjadi 2 sama besar, misal l1 dan l2. Jika panjang list ganjil,
      maka l1 akan memiliki 1 elemen lebih banyak dibanding l2
   3. Ambil elemen terkecil dari l1, masukkan ke akhir l3.
   4. Ambil elemen terbesar dari l2, masukkan ke akhir l3.
   5. Ulangi langkah 3 dan 4 sampai kedua list kosong. -}

sortList :: [Int] -> [Int]
{- Mengurutkan list of integer l dari elemen yang terkecil ke terbesar -}
delElmt ::  Int -> [Int] -> [Int]
{- Menghapus elemen X integer dari list of integer l -}
getSmallest :: [Int] -> Int
{- Mengambil nilai integer terkecil dari list of integer l -}

-- REALISASI
alternateSort l =
    let li = sortList l
    in
        if isOneElmt li || isEmpty li then li
        else konsoList [head li, last li] (alternateSort (tail (init li)))

getSmallest l =
    if isOneElmt l then head l                              -- basis
    else if head l <= getSmallest (tail l) then head l      
    else getSmallest (tail l)                               -- rekurens

delElmt x l =   
    if isEmpty l then []                                    -- basis
    else if head l == x then tail l                         -- rekurens
    else konso (head l) (delElmt x (tail l))

sortList l =
    if isOneElmt l then l                                   -- basis
    else konso (getSmallest l) (sortList (delElmt (getSmallest l) (l))) -- rekurens