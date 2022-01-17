
import sys,time
import os
# ========================>>> DICTIONARI NILAI TIAP SLES IP ADDRESS
DB_SubnetMaskIP = {
    "/8" :    "255.0.0.0",
    "/9" :    "255.128.0.0",
    "/10":    "255.192.0.0",
    "/11":    "255.224.0.0",
    "/12":    "255.240.0.0",
    "/13":    "255.248.0.0",
    "/14":    "255.252.0.0",
    "/15":    "255.254.0.0",
    "/16":    "255.255.0.0",
    "/17":    "255.255.128.0",
    "/18":    "255.255.192.0",
    "/19":    "255.255.224.0",
    "/20":    "255.255.240.0",
    "/21":    "255.255.248.0",
    "/22":    "255.255.252.0",
    "/23":    "255.255.254.0",
    "/24":    "255.255.255.0",
    "/25":    "255.255.255.128",
    "/26":    "255.255.255.192",
    "/27":    "255.255.255.224",
    "/28":    "255.255.255.240",
    "/29":    "255.255.255.248",
    "/30":    "255.255.255.252",
    "/31":    "255.255.255.254"
}
# ===========================DICTIONARY BINARY IP
DB_binari = {
    "/8" :    "11111111.00000000.00000000.00000000",
    "/9" :    "11111111.10000000.00000000.00000000",
    "/10":    "11111111.11000000.00000000.00000000",
    "/11":    "11111111.11100000.00000000.00000000",
    "/12":    "11111111.11110000.00000000.00000000",
    "/13":    "11111111.11111000.00000000.00000000",
    "/14":    "11111111.11111100.00000000.00000000",
    "/15":    "11111111.11111110.00000000.00000000",
    "/16":    "11111111.11111111.00000000.00000000",
    "/17":    "11111111.11111111.10000000.00000000",
    "/18":    "11111111.11111111.11000000.00000000",
    "/19":    "11111111.11111111.11100000.00000000",
    "/20":    "11111111.11111111.11110000.00000000",
    "/21":    "11111111.11111111.11111000.00000000",
    "/22":    "11111111.11111111.11111100.00000000",
    "/23":    "11111111.11111111.11111110.00000000",
    "/24":    "11111111.11111111.11111111.00000000",
    "/25":    "11111111.11111111.11111111.10000000",
    "/26":    "11111111.11111111.11111111.11000000",
    "/27":    "11111111.11111111.11111111.11100000",
    "/28":    "11111111.11111111.11111111.11110000",
    "/29":    "11111111.11111111.11111111.11111000",
    "/30":    "11111111.11111111.11111111.11111100",
    "/31":    "11111111.11111111.11111111.11111110"
}

#======================DICTIONARY BANYAK HOST 
DB_host = {
    "/8" :    "16,777,216 Host",
    "/9" :    "8,388,608 Host",
    "/10":    "4,194,304 Host",
    "/11":    "2,097,152 Host",
    "/12":    "1,048,576 Host",
    "/13":    "524.288 Host",
    "/14":    "264.144 Host",
    "/15":    "131.072 Host",
    "/16":    "65.536 Host",
    "/17":    "32.768 Host",
    "/18":    "16.384 Host",
    "/19":    "8.192 Host",
    "/20":    "4.096 Host",
    "/21":    "2.048 Host",
    "/22":    "1.024 Host",
    "/23":    "512 Host",
    "/24":    "256 Host",
    "/25":    "128 Host",
    "/26":    "64 Host",
    "/27":    "32 Host",
    "/28":    "16 Host",
    "/29":    "8 Host",
    "/30":    "4 Host",
    "/31":    "2 Host"
}

def ketik(text):
    for i in text + "\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)

# ==========================>>> PENGKONDISIAN STATUS KELAS IP ADDRESS
# 09-15 kelas A
# 16-23 kelas B
# 24-30 kelas C

DB_kelasip = {
    "/8" :    "KELAS A",
    "/9" :    "KELAS A",
    "/10":    "KELAS A",
    "/11":    "KELAS A",
    "/12":    "KELAS A",
    "/13":    "KELAS A",
    "/14":    "KELAS A",
    "/15":    "KELAS A",
    "/16":    "KELAS B",
    "/17":    "KELAS B",
    "/18":    "KELAS B",
    "/19":    "KELAS B",
    "/20":    "KELAS B",
    "/21":    "KELAS B",
    "/22":    "KELAS B",
    "/23":    "KELAS B",
    "/24":    "KELAS C",
    "/25":    "KELAS C",
    "/26":    "KELAS C",
    "/27":    "KELAS C",
    "/28":    "KELAS C",
    "/29":    "KELAS C",
    "/30":    "KELAS C",
    "/31":    "KELAS C"
}

# LIST OKTET=============
listoktet=[]
# ==========================




nama = input("Masukkan Nama : \t")
os.system('cls')
ketik("SELAMAT DATANG %s " %nama)

# input slash
while True:
    inputslesIP = input("Masukkan slas( /8 - /30 ) IP Address = \t" )
    print("\n")
    if len(inputslesIP)==3 or 2 and "/" in inputslesIP:
        break

# input ip
while True:
    inputIpAddress = input("Masukkan IP Address: \t")
    if len(inputIpAddress) <= 15 and "." in inputIpAddress:
        break
    else:
        print(inputIpAddress)

os.system('cls')
print(f"=============DETAIL STATUS IP============= ")

# menampilkan ip
Mip = inputIpAddress
print(f"Ip Address \t:", Mip)
# Menampilkan kelas
MkelasIP = DB_kelasip[inputslesIP]
print(f"Status IP  \t:", MkelasIP)
# menampilkan SubnetMask IP
Msubnetmask = DB_SubnetMaskIP[inputslesIP]
print (f"Subnet Mask \t:", Msubnetmask)
#  menampilkan banyak host
Mhost = DB_host[inputslesIP]
print (f"Jumlah Host \t:", Mhost)
# menampilkan binery
Mbinary = DB_binari[inputslesIP]
print (f"Binary \t\t:", Mbinary)


# Menampilkan range ip

#==============================PENGULANGAN UNTUK RANGE IP
if MkelasIP == "KELAS A":
    # script pengulangan untuk range IP kelas A
    oktetkelasA = int(Msubnetmask[4:7])
    hasiloktetA = int(256) - int(oktetkelasA)
    oktetkonstanA = hasiloktetA
    while hasiloktetA < 256:
        hasiloktetA = hasiloktetA + oktetkonstanA
        
        listoktet.append(hasiloktetA)
elif MkelasIP == "KELAS B":
    # script pengulangan untuk range IP kelas B
    oktetkelasB = int(Msubnetmask[8:11])
    hasiloktetB = int(256) - int(oktetkelasB)
    oktetkonstanB = hasiloktetB
    while hasiloktetB < 256:
        hasiloktetB = hasiloktetB + oktetkonstanB
       
        listoktet.append(hasiloktetB)
else:
    # script pengulangan untuk range IP kelas C
    oktetkelasC = int(Msubnetmask[12:15])
    hasiloktetC = int(256) - int(oktetkelasC)
    oktetkonstanC = hasiloktetC
    while hasiloktetC < 256:
        hasiloktetC = hasiloktetC + oktetkonstanC
        
        listoktet.append(hasiloktetC)



if len(listoktet) < 4:
    print ("Range IP "+"\t:0", listoktet[0], listoktet[1], "dan seterusnya...")
else:
    print ("Range IP \t:",[0], listoktet[1], listoktet[2], listoktet[3], listoktet[4])
    



print("=======================================================")





