module SeleksiKerja where

-- SELEKSI KERJA                                        seleksi(m, s, p) 

-- DEFINISI DAN SPESIFIKASI
seleksi :: Int -> Int -> Char -> Bool
{- seleksi(m, s, p) mengecek apakah seseorang dapat masuk ke perusahaan 'p' dengan pengalaman managerial 'm' dan software engineer 's' yang ia punya
   - Jika pelamar memiliki pengalaman managerial >= 2 tahun dan memiliki pengalaman menjadi software engineer >= 4 tahun, maka ybs bisa mendaftar untuk semua pekerjaan.
   - Jika pelamar memiliki kemampuan managerial < 2 tahun namun memiliki pengalaman menjadi software engineer >= 4 tahun, maka ybs bisa mendaftar untuk
     pekerjaan B. Selain itu, jika pengalaman menjadi software engineernya < 4 tahun, maka ybs hanya dapat mendaftar untuk pekerjaan C.
   - Jika pengalaman menjadi software enginnernya < 4 tahun namun memiliki pengalaman managerial >= 2 tahun, maka ybs dapat mendaftar untuk pekerjaan D.
   - Semua pelamar dapat melamar untuk pekerjaan C. -}

-- REALISASI
seleksi m s p
    | (p == 'A') = (m >= 2) && (s >= 4)
    | (p == 'B') = (s >= 4)
    | (p == 'C') = True
    | (p == 'D') = (m >= 2)
