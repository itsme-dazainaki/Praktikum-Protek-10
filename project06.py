nama = input("Masukkan nama file: ") #ini untuk input nama file
n = int(input("Masukkan nilai n  : ")) #ini untuk input nilai dari n
inputan = open(nama, "r") #membuka file berdasar inputan yang tadi
teks = inputan.read() #membaca isi file diatas
isi = list(teks) #mengubah isi dari pembacaan file text char menjadi list

sandi = []  #deklarasikan sandi sebagai list yang kosong
for i in isi: #perulangan pengecekan (var i) yang berada di range data isi
    ascii1 = ord(i) #mengubah karakter ke nilai ASCII    
    if ascii1 == 32: #jika jumlah char sama dengan 32 maka
        ascii2 = ascii1 #nilai ascii sama dan tidak dirubah
    else:  #jika jum char != 32 maka
        ascii2 = ascii1 + n #geser ascii sebanyak n langkahs
        if ascii2 > 122: #jika jum char ascii > 122 maka
            ascii2 = ascii2 - 26 #kurangi jum char ascii sebanyak 26
        elif ascii2 > 90 and ascii2 <97 : # jika jum char ascii 91-96 maka
            ascii2 = ascii2 - 26 #kurangi jum char asciisebanyak 26
    a = chr(ascii2) #buat variabel a dan ubah ascii menjadi huruf
    sandi = sandi +[a] #isi nilai tadi var tersandi
    if not isi : #jika tidak memenuhi syarat maka
        break #hentikan perulangan

caesar = "".join(sandi) #menggabung karakter yang telah disandi
hasil = open("fileenkripsi.txt", "w") #membuka file dengan opsi write
hasil.write(caesar) #menulis hasil penyandian ke file baru
hasil.close() #tutup file untuk mencegah file corrupted atau strukturnya rusak 
hasilsandi = open("fileenkripsi.txt", "r") ##membuka file dengan opsi read
print(hasilsandi.read()) #tampilkan pembacaan file hsail sandi
hasilsandi.close() #tutup file untuk mencegah file corrupted atau strukturnya rusak 