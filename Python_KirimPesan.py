import sys, time 
import os
from random import random




# =============TEMPAT FUNCTION==================

def spin():
    try:
        L="/-\\|"
        for q in range (100):
            time.sleep(0.1)
            sys.stdout.write("\r["+L[q % len(L)]+"]")
            sys.stdout.flush()
    except:
            exit()

def nama(namaU):
    print("===============Selamat Datang %s ===============" %namaU.upper() )


def akun(namadepan, namabelakang, email, nomorhp, jeniskelamin, alamat ):
    print (f"Nama Depan anda : \t {namadepan}")
    print (f"Nama Belakang anda : \t {namabelakang}")
    print (f"Email anda : \t {email}")
    print (f"Jenis Kelamin : \t {jeniskelamin}")
    print (f"Nomor Handphone : \t {nomorhp}")
    print (f"Alamat : \t {alamat}" )
    print (f"Username anda {email}@DESmash.com")
    print (f"Password Akun Anda adalah : {random()}")
    return

def buatakun():
    while True:
        try:
            namadepan = str( input ("Ketikkan Nama Depan Anda :"))
            if namadepan.isalpha():
                break
            else :
                print ("Ketikkan Nama Depan Anda Dengan Benar (tanpa space ataupun karakter lainnya")
        except:
            print ("HARAP MASUKKAN NAMA DEPAN DENGAN BENAR")
    time.sleep(5)

    while True :
        try:
            namabelakang = str(input("Ketikkan Nama Belakang Anda :"))
            if namabelakang.isalpha():
                break
            else:
                print ("Ketikkan Nama Belakang Anda Dengan Benar (tanpa space ataupun karakter lainnya")
        except:
            print ("HARAP MASUKKAN NAMA BELAKANG DENGAN BENAR")
    time.sleep(5)

    while True:
        try:
            email=str (input("Ketik Alamat Email Anda : "))
            if email.isalpha():
                break
            else:
                print ("Ketikkan Email Anda Dengan Benar (tanpa space ataupun @gmail.com")
        except :
            print ("HARAP MASUKKAN EMAIL DENGAN BENAR")
    time.sleep(5)

    while True:
        try:
            nomorhp = str(input("Ketikkan Nomor HP anda : "))
            if nomorhp.isdecimal():
                break
            else:
                print ("Ketikkan Nomor Handphone Anda Dengan Benar (tanpa space ataupun karakter +62")
        except:
            print ("HARAP MASUKKAN NOMOR HANDPHONE DENGAN BENAR")
    time.sleep(5)

    while True :
        try:
            jeniskelamin = str(input ("Jenis Kelamin : "))
            if jeniskelamin.isalpha:
                break
            else:
                print ("Ketikkan Jenis Kelamin Anda Dengan Benar (tanpa space ataupun karakter lainnya")
        except:
            print ("HARAP MASUKKAN JENIS KELAMIN DENGAN BENAR")

    time.sleep(5)
    while True :
        try :
            alamat = str(input("Ketikkan Alamat Anda : "))
            if alamat.isalpha :
                break
            else:
                print ("Ketikkan Alamat Anda Dengan Benar (tanpa space ataupun karakter lainnya")
        except:
            print ("HARAP MASUKKAN ALAMAT DENGAN BENAR")
    os.system('clear')
    spin()
    print("================== PROFILE ANDA ==================")
    akun(namadepan, namabelakang, email, nomorhp, jeniskelamin, alamat )

# =================================================
# keterangan
ket1=""" Program ini bernama DESmash, berfungsi untuk mengirim pesan kepada nomor tujuan yang anda inginkan\n
kami membuat program ini semata-mata hanya untuk menghilangkan kegabutan. \n
selain itu, kami juga berharap program ini bisa berguna bagi anda.\n
D.Leo
"""

ket2 = """
===============CARA MENGGUNAKAN DESmash=============== \n
1. Buat akun terlebih dahulu
2. Ingatlah Pin anda
3. Gunakan program DESmash
4. Ketikkan nomor tujuan
5. Masukkan PIN yang sudah diberikan sebelumnya
6. Tunggu sampai notifikasi muncul
"""

# ===========TEMPAT MENARUH LIST======================


# =================================================

namaU = str (input ("Masukkan Nama Anda \t"))
os.system('clear')
nama(namaU)

print("""
[1] READme  \t  [3] Buat Akun 
[2] Tutorial \t [4] DESmash
""")

while True :
    try:
        pilihan = int(input("Pilih Menu di Atas :\t"))
        if pilihan == 1 :
            print(ket1)
            break
        elif pilihan ==2:
            print(ket2)
            break           
        elif pilihan ==3:
            buatakun()
            break
        elif pilihan == 4:
            print("desmash")
            break
        else:
            print("Masukkan angka yang tertera pada menu diatas!")
    except:
        print("HARAP MASUKKAN PILIH MENU YANG BENAR")


while True :
    try:
        Username=str(input("Username :"))
        if Username.isalpha():
            break
        else :
            print("Username anda salah")
    except:
        print("SILAHKAN MASUKKAN USERNAME ANDA DENGAN BENAR")

while True :
    try:
        Password=str(input("PIN :"))
        if Username.isdecimal():
            break
        else :
            print("PIN anda salah")
    except:
        print("SILAHKAN MASUKKAN PIN ANDA DENGAN BENAR")




    




