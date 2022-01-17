import sys, time
import sys,time

def spin():
    try:
        L="/-\\|"
        for q in range (10):
            time.sleep(0.1)
            sys.stdout.write("\r["+L[q % len(L)]+"]")
            sys.stdout.flush()
    except:
            exit()


def ketik(text):
    for i in text + "\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)



def penjumlahan():   
    a = int(input("masukkan angka pertama: \t"))
    b = int(input("masukkan angka kedua: \t\t"))  
    print("======================================")
    hasil = a+b
    spin()
    "\n"
    ketik (f"Hasil dari penjumlahan {a} + {b} = {hasil}")

def pengurangan():   
    a = int(input("masukkan angka pertama: \t"))
    b = int(input("masukkan angka kedua: \t\t"))  

    print("======================================")
    hasil = a-b
    spin()
    "\n"
    ketik (f"Hasil dari pengurangan {a} - {b} = {hasil}")

def pembagian():   
    a = int(input("masukkan angka pertama: \t"))
    b = int(input("masukkan angka kedua: \t\t"))  

    print("======================================")
    hasil = a/b
    spin()
    "\n"
    ketik (f"Hasil dari pembagian {a} / {b} = {hasil}")

def perkalian():   
    a = int(input("masukkan angka pertama: \t"))
    b = int(input("masukkan angka kedua: \t\t"))  

    print("======================================")
    hasil = a*b
    spin()
    "\n"
    ketik(f"Hasil dari perkalian {a} * {b} = {hasil}")

print("***********************************************************")
print("***********SELAMAT DATANG DI KALKULATOR DEPYTHON***********")
print("***********************************************************")

print('\n')

print("Silahkan pilih operasi yang akan anda lakukan")
print(
"\n"
"[1] Penjumlahan \t [3] Pembagian "
"\n"
"[2] Pengurangan \t [4] Perkalian"
)
while True:


    try:
        pilihan = int(input("Masukkan Nomor Pilihan Anda >>> "))
        print("\n")
        if pilihan == 1:
            penjumlahan()
            break
        elif pilihan == 2:
            pengurangan()
            break
        elif pilihan == 3:
            pembagian()
            break
        elif pilihan ==4 :
            perkalian()
            break
        else:
            print("Harap Masukkan Nomor yang tertera di atas!!")
    except:
        ketik("PASTIKAN ANDA MENGETIKKAN NOMOR YANG TERTERA DIATAS")
    

          
 
    