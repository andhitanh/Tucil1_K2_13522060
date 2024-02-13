# Tucil1_K2_13522060_Andhita Naura Hariyanto
Tugas Kecil 1 IF2211 Strategi Algoritma - Penyelesaian Cyberpunk 2077 Breach Protocol dengan Algoritma Brute Force

## Table of Contents
* [General Information](#general-information)
* [Creator](#creator)
* [Features](#features)
* [Requirements](#requirements)
* [How to Run](#how-to-run)
* [Repository Structure](#repository-structure)

## General Information
Program ini menggunakan Algoritma Brute Force untuk menyelesaikan persoalan pencarian optimal pola dengan nilai terbesar yang terinspirasi dari permasalahan Breach Protocol pada permainan Cyberpunk 2077. Program akan menerima masukan berupa data token, matriks dari token, ukuran buffer, sekuens, dan nilai dari tiap sekuens. Kemudian, program akan mengembalikan data pola token yang memberikan nilai reward paling optimal jika pola token paling optimal terdapat pada matriks token.

## Creator
| NIM      | Nama                    | Kelas                                                                                                                                                                                                               |
|----------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 13522060 | Andhita Naura Hariyanto    | K-02                                                              |

## Features
- Menampilkan solusi Permainan Cyberpunk 2077 Beach Protocol berdasarkan input data matriks dan sekuens dari pengguna.
- Menampilkan solusi Permainan Cyberpunk 2077 Beach Protocol berdasarkan matriks dan sekuens yang dipilih secara random.
- Menyimpan solusi Permainan Cyberpunk 2077 Beach Protocol ke dalam file .txt yang akan tersimpan dalam folder test/output

## Requirements
Anda harus menginstall bahasa python untuk menjalankan program ini.

## How to Run
1. Buka terminal and clone repository berikut (https://github.com/andhitanh/Tucil1_K2_13522060.git)

2. Buka folder src dengan menjalankan command berikut pada folder utama di
```
cd src
```

3. Jalankan program utama dengan perintah berikut

```
python main.py
```

## Repository Structure
```
+---bin
+----------build  
+----------dist
|           main.exe
|       main.spec
|
+---doc
|       Tucil1_K2_13522060_Andhita Naura Hariyanto.pdf
|
+---src
|       main.py
|       randomize.py
|       sekuens.py
|       tokens.py
|       tree.py
|
+---test
+----------output                
|               testcase1output.txt
|               testcase2output.txt
|               testcase4output.txt
|               testcase6output.txt
|               testcase7output.txt
|       testcase1.txt
|       testcase2.txt
|       testcase3.txt
|       testcase4.txt
|       testcase5.txt
|       testcase6.txt
```