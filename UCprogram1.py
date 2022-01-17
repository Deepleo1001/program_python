subnetmask = input ("masukkan subnetmask :\t")

print (subnetmask)
codesubnet = subnetmask[12:15]
print("bagian oktet terakhir subnetmask %s"% codesubnet)
hasilcs = int(256) - int(codesubnet)
print (hasilcs)
listhasilcs =[]
hasilcskonstan=hasilcs

while hasilcs < 250:
    hasilcs = hasilcs + hasilcskonstan
    listhasilcs.append(hasilcs)
print(listhasilcs[0], listhasilcs[1] )







    
    
    

