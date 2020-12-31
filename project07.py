fileasli = open("fileenkripsi.txt", "r") #membuka file dengan opsi read/baca
n = int(input("Masukkan nilai n: ")) #input berupa berupa nilai n
teks = fileasli.read() #ini syntax untuk membaca file text yang ada di atas
isi = list(teks) #ini untuk mengubah isi ke bentuk data list

unsandi = [] #deklarasikan sandi sebagai list yang kosong
for i in isi: #perulangan pengecekan (var i) yang berada di range data isi    
    ascii1 = ord(i) #mengubah karakter ke nilai ASCII
    if ascii1 == 32: #jika jumlah char sama dengan 32 maka
        ascii2 = ascii1 #nilai ascii sama dan tidak dirubah
    else: #jika jum char != 32 maka
        ascii2 = ascii1 - n #geser ascii sebanyak n langkahs
        if ascii2 < 65: #jika jum char ascii < 65 maka
            ascii2 = ascii2 + 26  #tambahkan jum char ascii sebanyak 26
        elif (90 < ascii2 and ascii2 <97):  #jika jum char ascii 91-96 maka
            ascii2 = ascii2 + 26 #tambahkan jum char ascii sebanyak 26   
    a = chr(ascii2) #buat variabel a dan ubah ascii menjadi huruf
    unsandi.append(a) #menambahkan var diatas ke list tado

teksasli = "".join(unsandi) #menggabngkan data dalam list hasil
hasil = open("hasil07.txt", "w") #membuka file hasil dengan opsi write/tulis data
hasil.write(teksasli) #menuliskan terjemahan ke file tujuan
hasil.close() #tutup file untuk mencegah file corrupted atau strukturnya rusak 
hasilsandi = open("hasil07.txt", "r") ##membuka file dengan opsi read
print(hasilsandi.read()) #tampilkan pembacaan file hsail sandi
fileasli.close() #tutup file untuk mencegah file corrupted atau strukturnya rusak 