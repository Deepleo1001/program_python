baris1A =[]
baris2A =[]
baris3A =[]

print("""
================ INPUT DATA MATRIX A ================
""")
while True:
    matrix1A = input("Masukkan angka baris pertama ")
    if len(matrix1A) == 8:
        baris1A.append(matrix1A)
        break
    else:
        print("\n===Contoh input yang benar 22,22,22 (Minimal 2 Angka dan 2 titik koma===\n")
    
while True:
    matrix2A = input("Masukkan angka baris kedua ")
    if len(matrix2A) == 8:
        baris2A.append(matrix2A)
        break
    else:
        print("\n===Contoh input yang benar 22,22,22 (Minimal 2 Angka dan 2 titik koma===\n")

while True:
    matrix3A = input("Masukkan angka baris ketiga ")
    if len(matrix3A) == 8:
        baris3A.append(matrix3A)
        break
    else:
        print("\n===Contoh input yang benar 22,22,22 (Minimal 2 Angka dan 2 titik koma===\n")

Atitik1_1= int(matrix1A[0:2]) 
Atitik1_2= int (matrix1A[3:5])
Atitik1_3= int (matrix1A[6:8])
Atitik2_1= int (matrix2A[0:2])
Atitik2_2= int (matrix2A[3:5])
Atitik2_3= int (matrix2A[6:8])
Atitik3_1= int (matrix3A[0:2])
Atitik3_2= int (matrix3A[3:5])
Atitik3_3= int (matrix3A[6:8])



baris1B =[]
baris2B =[]
baris3B =[]

print("""
================ INPUT DATA MATRIX B ================
""")

while True:
    matrix1B = input("Masukkan angka baris pertama ")
    if len(matrix1B) == 8:
        baris1B.append(matrix1B)
        break
    else:
        print("\n===Contoh input yang benar 22,22,22 (Minimal 2 Angka dan 2 titik koma===\n")

while True:
    matrix2B = input("Masukkan angka baris kedua ")
    if len(matrix2B) == 8:
        baris2B.append(matrix2B)
        break
    else:
        print("\n===Contoh input yang benar 22,22,22 (Minimal 2 Angka dan 2 titik koma===\n")

while True:
    matrix3B = input("Masukkan angka baris ketiga ")
    if len(matrix3B) == 8:
        baris3B.append(matrix3B)
        break
    else:
        print("\n===Contoh input yang benar 22,22,22 (Minimal 2 Angka dan 2 titik koma===\n")

Btitik1_1= int(matrix1B[0:2]) 
Btitik1_2= int (matrix1B[3:5])
Btitik1_3= int (matrix1B[6:8])
Btitik2_1= int (matrix2B[0:2])
Btitik2_2= int (matrix2B[3:5])
Btitik2_3= int (matrix2B[6:8])
Btitik3_1= int (matrix3B[0:2])
Btitik3_2= int (matrix3B[3:5])
Btitik3_3= int (matrix3B[6:8])


# Perkalian
kali1_1=Atitik1_1 * Btitik1_1
kali1_2=Atitik1_2 * Btitik1_2
kali1_3=Atitik1_3 * Btitik1_3
kali2_1=Atitik2_1 * Btitik2_1
kali2_2=Atitik2_2 * Btitik2_2
kali2_3=Atitik2_3 * Btitik2_3
kali3_1=Atitik3_1 * Btitik3_1
kali3_2=Atitik3_2 * Btitik3_2
kali3_3=Atitik3_3 * Btitik3_3

#penjumlahan
tambah1_1=Atitik1_1 + Btitik1_1
tambah1_2=Atitik1_2 + Btitik1_2
tambah1_3=Atitik1_3 + Btitik1_3
tambah2_1=Atitik2_1 + Btitik2_1
tambah2_2=Atitik2_2 + Btitik2_2
tambah2_3=Atitik2_3 + Btitik2_3
tambah3_1=Atitik3_1 + Btitik3_1
tambah3_2=Atitik3_2 + Btitik3_2
tambah3_3=Atitik3_3 + Btitik3_3

#Pengurangan
kurang1_1=Atitik1_1 - Btitik1_1
kurang1_2=Atitik1_2 - Btitik1_2
kurang1_3=Atitik1_3 - Btitik1_3
kurang2_1=Atitik2_1 - Btitik2_1
kurang2_2=Atitik2_2 - Btitik2_2
kurang2_3=Atitik2_3 - Btitik2_3
kurang3_1=Atitik3_1 - Btitik3_1
kurang3_2=Atitik3_2 - Btitik3_2
kurang3_3=Atitik3_3 - Btitik3_3



print("\n")
print("Matrix A \t Matrix B")
print(baris1A, '\t',baris1B)
print(baris2A, '\t',baris2B)
print(baris3A, '\t',baris3B)
print("\n")

print("""
\t DAFTAR MENU
====================================
[1] PENJUMLAHAN
[2] PENGURANGAN
[3] PERKALIAN
""")
while True:
    pilih= input("Pilihlah salah satu menu diatas\t:")
    if pilih == "1":
        print("\n")
        print("Matrix A \t Matrix B")
        print(baris1A, '\t',baris1B)
        print(baris2A, '\t',baris2B)
        print(baris3A, '\t',baris3B)
        print("\n")

        print("======HASIL PENJUMLAHAN======\n")
        print (f"[{tambah1_1},{tambah1_2},{tambah1_3}]")
        print (f"[{tambah2_1},{tambah2_2},{tambah2_3}]")
        print (f"[{tambah3_1},{tambah3_2},{tambah3_3}]")
    elif pilih == "2":
        print("\n")
        print("Matrix A \t Matrix B")
        print(baris1A, '\t',baris1B)
        print(baris2A, '\t',baris2B)
        print(baris3A, '\t',baris3B)
        print("\n")
        print("======HASIL PENGURANGAN======\n")
        print (f"[{kurang1_1},{kurang1_2},{kurang1_3}]")
        print (f"[{kurang2_1},{kurang2_2},{kurang2_3}]")
        print (f"[{kurang3_1},{kurang3_2},{kurang3_3}]")
    elif pilih=="3":
        print("\n")
        print("Matrix A \t Matrix B")
        print(baris1A, '\t',baris1B)
        print(baris2A, '\t',baris2B)
        print(baris3A, '\t',baris3B)
        print("\n")
        print("======HASIL PERKALIAN======\n")
        print (f"[{kali1_1},{kali1_2},{kali1_3}]")
        print (f"[{kali2_1},{kali2_2},{kali2_3}]")
        print (f"[{kali3_1},{kali3_2},{kali3_3}]")
    else:
        print("SILAHKAN INPUTKAN PILIHAN YANG BENAR")
        





