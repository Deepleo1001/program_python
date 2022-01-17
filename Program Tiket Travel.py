print (" \t PENJUALAN TIKET TRAVEL")
print("=========================================")

nama_pembeli = input(str("Nama Pembeli \t:"))

while True:
    jenis_tiket = input(str("Jenis Tiket [ B/K/P ] \t:"))

    if jenis_tiket == "B" :
        print("""
        \t Daftar Tiket
        ============================
        \n
        Tiket B
        1. PTK-SKD [ID : 0B1]
        2. PTK-STN [ID : 0B2]
        """)
        break
    elif jenis_tiket == "K":
        print("""
        \t Daftar Tiket
        ============================
        Tiket K
        1. PTK-SMG [ID : 0K1]
        2. PTK-SUB [ID : 0K2]
        3. PTK-JKT [ID : 0K3]
        """)
        break
    elif jenis_tiket == "P":
        print("""
        \t Daftar Tiket
        ============================
        Tiket P
        1. PTK-JKT [ID : 0P1]
        2. PTK-YGY [ID : 0P2]
        3. PTK-SOL [ID : 0P3]
        4. PTK-SUB [ID : 0P4]
        """)
        break
    else:
        print("===============================================")
        print("Maaf Mohon Inputkan Jenis Tiket Dengan Benar!!")
        print("===============================================")




input_pilihan = str(input("Masukkan Nomor ID Tiket \t:"))
if input_pilihan == "0B1" :
    print ("Harga Tiket : Rp60.000")
    harga_tiket = 60000
elif input_pilihan == "0B2" :
    print ("Harga Tiket : Rp120.000")
    harga_tiket = 120000
elif input_pilihan == "0K1" :
    print ("Harga Tiket : Rp160.000")
    harga_tiket = 160000
elif input_pilihan == "0K2" :
    print ("Harga Tiket : Rp195.000")
    harga_tiket = 195000
elif input_pilihan == "0K3" :
    print ("Harga Tiket : Rp1.250.000")
    harga_tiket = 1250000
elif input_pilihan == "0P1" :
    print ("Harga Tiket : Rp450.000")
    harga_tiket = 450000
elif input_pilihan == "0P2" :
    print ("Harga Tiket : Rp950.000 ")
    harga_tiket = 950000
elif input_pilihan == "0P3" :
    print ("Harga Tiket : Rp925.000")
    harga_tiket = 925000
elif input_pilihan == "0P4" :
    print ("Harga Tiket : Rp1.200.000 ")
    harga_tiket = 1200000
else:
    print("-")


jumlah_beli = int(input("Jumlah Tiket Yang Dibeli \t:"))
print("================================================")
total_beli= harga_tiket* jumlah_beli
print(f"Total Beli \t: {total_beli}")
pembayaran = int(input("Masukkan Total Pembayaran \t:"))
Kembalian = pembayaran - total_beli
print(f"Kembalian \t: {Kembalian}")















