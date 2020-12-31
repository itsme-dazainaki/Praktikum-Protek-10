myfile = open("pro02.txt" , "r") #buka file text dengan pilihan mode untuk "read"
baris = myfile.readlines()  #ini syntax untuk membaca file text yang ada diatas

dict = {} #deklarasikan dictionary yang kosong
list = [] #deklarasikan list yang kosong
for i in range(len(baris)): #pengecekan (var i) yang berada di range data hasil pembacaan pro02.txt menggunakan perulangan
    a = baris[i].split("|") #membuat var a yang berisi data hasil pembacaan dan memisahkannya berdasar char "|"
    a[2] = a[2].replace("\n", "") #untuk data no 3, replace /n dengan karakter kosong
    dict = {"nim" : a[0], "nama" : a[1], "alamat" : a[2]} #isi dictionary tadi dengan list data hasil split
    list.append(dict) #tambahkan data diatas ke list 

print(list) #tampilkan semua data yang ada pada list dictionary
myfile.close() #tutup file untuk mencegah file corrupted atau strukturnya rusak 
