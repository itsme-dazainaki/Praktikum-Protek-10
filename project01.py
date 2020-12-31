myfile = open("pro01.txt", "r") #buka file text dengan pilihan mode untuk "read"
teks = myfile.readlines() #ini syntax untuk membaca file text yang ada di atas

ganjil = [] #deklarasikan ganjil sebagai list yang kosong
genap = [] #deklarasikan genap sebagai list yang kosong
for i in range(len(teks)): #perulangan untuk data yang ada di rentang text, hasil pembacaan file
        if (int(teks[i])%2 != 0): #jika dalam data yang dicek dibagi 2 dan sisanya tidak 0, maka
            ganjil.append(teks[i]) #tambahkan 1 data hasil pengecekan tadi ke list ganjil
        else :
            genap.append(teks[i]) #tambahkan 1 data hasil pengecekan diluar kondisi tadi ke list ganjil

print ("Banyaknya bilangan Ganjil : {0}".format(len(ganjil))) #tampilkan jumlah anggota list ganjil
print ("Banyaknya bilangan Genap : {0}".format(len(genap))) #tampilkan jumlah anggota list genap
myfile.close()  #tutup file untuk mencegah file corrupted atau strukturnya rusak      