inputan = open("pro05.txt", "r") #buka file text dengan pilihan mode untuk "read"
output = open("hasil05.txt", "w") #buka file text dengan pilihan mode "write"
data = inputan.readlines()  #ini syntax untuk membaca file text yang ada di atas

for i in range(len(data)):  #perulangan pengecekan (var i) yang berada di range teks hasil pembacaan pro02.txt 
    bil = data[i].split("|") #membuat var a yang berisi data hasil pembacaan dan memisahkannya berdasar char "|"
    jum = int(bil[0]) + int(bil[1]) #ini rumus jum, operasi penjumlahan antara data list index 0 dan 1
    hasil = str(jum) #rubah format hasil penjumlahan diatas menjadi string
    output.write(hasil) #tulis data diatas ke file text output
    output.write("\n") #tuliskan new line agar hasil ditambahkan secara vertikal
output.close() #tutup file untuk mencegah file corrupted atau strukturnya rusak 

hasil05 = open("hasil05.txt", "r") #buka file text dengan pilihan mode untuk "read"
print(hasil05.read()) #tampilkan pembacaan file hasil05
hasil05.close #tutup file untuk mencegah file corrupted atau strukturnya rusak 