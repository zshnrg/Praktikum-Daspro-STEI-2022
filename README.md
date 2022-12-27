# Praktikum Daspro STEI 2022
Repository ini berisi soal-soal dan pembahasan praktikum mata kuliah Daspro. File-file ini hanya boleh dijadikan referensi pembelajaran. Tidak semua file praktikum mendapatkan skor sempurna. Dilarang menduplikasi file untuk menjawab soal-soal praktikum.

## How to Haskell? ⬇️
Berikut ini beberapa langkah yang bisa kamu ikuti untuk menginstall Haskell yang saya rekomendasikan:
1. Instal Haskell melalui https://www.haskell.org/ghcup/
2. Salin command yang tersedia sesuai dengan Operating System yang dipakai. Jalankan pada Terminal/PowerShell.
Untuk Windows gunakan perintah ini pada PowerShell
```ps
Set-ExecutionPolicy Bypass -Scope Process -Force;[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; try { Invoke-Command -ScriptBlock ([ScriptBlock]::Create((Invoke-WebRequest https://www.haskell.org/ghcup/sh/bootstrap-haskell.ps1 -UseBasicParsing))) -ArgumentList $true } catch { Write-Error $_ }
```
3. Tampilan pertama akan meminta kamu untuk memilih direktori tempat meng-install. Tekan `Enter` untuk menggunakan direktori default.
4. Tampilan selanjutnya akan meminta kamu untuk memilih direktori tempat cabal di-install. Tekan `Enter` untuk menggunakan direktori default.
5. Selanjutnya kamu akan diberikan opsi untuk meng-install HSL, stack, dan MSys2. Tekan `Enter` pada ketiga pertanyaan untuk memilih opsi yang direkomendasikan.
6. Setelah MSys2 terpasang, sistem akan otomatis membuka GHCup installer. Tunggu hingga proses pemasangan selesai.
7. Haskell sudah berhasil dipasang :D

## Cara Menjalankan Program Haskell 🚶💨
Berikut ini merupakan cara menjalankan program Haskell sebagaimana program ditulis dalam bentuk modul sesuai dengan Diktat Perkuliahan yang digunakan pada IF1210 Dasar Pemrograman:
1. Buka terminal pada direktori program yang ingin dijalankan.
2. Jalankan GHCi untuk menjalankan compiler haskell yang interaktif dengan menggunakan command `ghci` pada terminal. Kondisi setelah berhasil dibuka kurang lebih seperti ini:
```ps
PS > ghci
GHCi, version 9.2.5: https://www.haskell.org/ghc/  :? for help
ghci>
```
3. Load modul yang telah dibuat pada file Haskell dengan menggunakan command:
```ps
ghci> :l Program.hs
```
4. Modul yang berhasil dimuat akan menapilkan pesan:
```ps
[1 of 1] Compiling Program             ( Program.hs, interpreted )
Ok, one module loaded.
ghci> 
```
5. Jalankan fungsi yang ingin digunakan dengan memanggil langsung fungsi beserta parameter yang digunakan. Contoh:

Program Haskell yang dibuat:
```haskell
module Kali where

-- KALI                                 kali(a,b)

-- DEFINISI DAN SPESIFIKASI
kali :: Int -> Int -> Int
{- kali(a,b) akan mengembalikan hasil kali bilangan integer
   a dan b -}

-- REALISASI
kali a b = a * b
```
Penggunaan fungsinya di terminal:
```ps
ghci> kali 2 4
8
ghci> kali 1 4
4
ghci> kali 12 10
120
```

## Kendala yang mungkin ditemukan 🤔
Apabila saat ingin menjalankan GHCi terdapat pesan error 
```
ghci : The term 'ghci' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
```
Pastikan bahwa command `ghci` sudah berada dalam PATH. Untuk memastikannya berikut adalah langkah-langkahnya:
1. Buka folder tempat GHCup terinstall. Secara default GHCup akan terinstall pada `C:\ghcup`.
2. Salin alamat tempat folder `bin` berada. Secara default folder ini akan berada pada `C:\ghcup\bin`.
3. Buka menu Start.
4. Buka program `Edit the system environment variables`.
5. Tekan `Environment Variables...`.
6. Klik dua kali pada variable `Path` di User variables.
7. Tambahkan alamat folder bin yang telah disalin apabila belum ada.
8. Tutup dan simpan perubahan.
9. Buka ulang Terminal/PowerShell dan jalankan `ghci`.
