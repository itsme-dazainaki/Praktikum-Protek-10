myfile = open("pro02.txt", "a") #buka file text dengan pilihan mode untuk "append" / menambah data
a = True #mari taruh nilai awal a
while ( a == True) : #pengecekan perulangan, jika a nilainya benar
    nim = input("Masukkan NIM : ") #ini untuk menginput data nim
    nama = input("Masukkan Nama Mahasiswa : ") #ini untuk menginput data nama
    alamat = input("Masukkan Alamat : ") #ini untuk menginput data alamat
    myfile.write(nim + "|" + nama + "|" + alamat + "\n")   #ini syntax untuk menambahkan data inputan diatas

    lagi = input("Apakah anda ingin mengulangi input (y/n) ? : ")  #input konfirmasi perulangan pengisian data
    if (lagi == "y") : #jika input "y" maka : 
        a = True #a bernilai benar, dan akan terjadi perulangan
    elif  (lagi == "n"):  #jika input "n" maka :
        a = False #a bernilai salah, dan tidak akan terjadi perulangan
    else : #jika inputan selain "y"/"n" maka :
        print ("Maaf !! input yang anda masukkan tidak valid") #akan tampil pesan berikut
    continue   
myfile.close() #tutup file untuk mencegah file corrupted atau strukturnya rusak 

