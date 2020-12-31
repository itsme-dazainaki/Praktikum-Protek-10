myfile = open("pro02.txt", "r")#buka file text dengan pilihan mode untuk "read"
teks = myfile.readlines()  #ini syntax untuk membaca file text yang ada di atas

nim = input("Masukkan NIM yang mau dicari: ") #ini untuk input nim yg akan kita cari
for i in range(len(teks)): #pengecekan (var i) yang berada di range teks hasil pembacaan pro02.txt menggunakan perulangan
    data = teks[i].split("|") #membuat var a yang berisi data hasil pembacaan dan memisahkannya berdasar char "|"
    if data[0] == nim : #jika data dgn nomor indeks[0] sama dengan nim yang tadi kita inputkan maka
        stat = "there" #status pengecekan menjadi there
        print("======= Data Mahasiswa ========") #tampilkan yang ada di blok print
        print("NIM    : ", data[0]) #tampilkan nim berasal dari data dgn nomor indeks[0]
        print("Nama   : ", data[1]) #tampilkan nama berasal dari data dgn nomor indeks[1]
        print("Alamat : ", data[2]) #tampilkan alamat berasal dari data dgn nomor indeks[2]
        break #hentikan perulangan jika sudah terpenuhi
    else: #jika tidak memenuhi kondisi maka
        stat = "none" #status pengecekan menjadi there
if stat == "none" :
    print("Maaf ! Data mahasiswa tidak ditemukan")
myfile.close()#tutup file untuk mencegah file corrupted atau strukturnya rusak 