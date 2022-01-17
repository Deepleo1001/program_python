datakotak =[ 'Nama : deepleo', 'Nomor :12773881267526167', 'Pekerjaan :sekertaris']

for i in (datakotak):
    print(i )

def inputkontak(nama, nomor, pekerjaan):
    datakotak.append("nama :%s" %nama)
    datakotak.append("nomor :%d" %nomor)
    datakotak.append("pekerjaan : %s" %pekerjaan)
    return


nama = input("masukkan nama :")
nomor = int(input("masukkan nomor :"))
pekerjaan = input("masukkan pekerjaan :")
inputkontak(nama,nomor,pekerjaan)



for i in (datakotak):
    print (i)
