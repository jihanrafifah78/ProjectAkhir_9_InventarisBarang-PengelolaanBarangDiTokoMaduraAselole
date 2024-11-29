daftar_barang = []
laporan_tambah = []
laporan_kurang = []
import datetime

def tampilan():
    print("\n==Pengelolaan Barang Di Toko==")
    print("1.Penambahan Barang")
    print("2.Tampilkan Barang")
    print("3.Update Barang")
    print("4.Hapus Barang")
    print("5.Kelompokkan Barang")
    print("6.Total")
    print("7.Pengurangan Barang")
    print("8.Laporan")
    print("9.Keluar")

def tanggal():
    while True:
        tanggal = input("Pilih Tanggal (Manual Atau Otomatis): ")
        if tanggal.lower() == "manual":
            return input("Masukkan Tanggal (yyyy-mm-dd): ")
        elif tanggal.lower() == "otomatis":
            return datetime.datetime.now().strftime("%Y-%m-%d")
        else:
            print("Masukkan Input Yang Bener Boss!!!")

def daftar_kategori():
    print("==Pilih Kategori Barang==")
    print("1.Makanan")
    print("2.Minuman")
    print("3.Alat Mandi")
    print("4.Bahan Masakan")
    print("5.Elektronik")

    while True:
        pilihan = input("Pilih Kategori: (1-5)")
        if pilihan == "1":
            return "Makanan"
        elif pilihan == "2":
            return "Minuman"
        elif pilihan == "3":
            return "Alat Mandi"
        elif pilihan == "4":
            return "Bahan Masakan"
        elif pilihan == "5":
            return "Elektronik"
        else:
            print("Masukkan Input Yang Bener Boss!!")
    
def id():
    while True:
        id = input("\nMasukkan ID Barang: (3 digit) ")
        if len(id) == 3 and id.isdigit():
            return id
        else:
            print("Masukkan Input Yang Benar!!!")

def banyak_barang():
    while True:
        banyak = input("Masukkan Banyak Barang: ")
        if banyak.isdigit():
            return int(banyak)
        else:
            print("Masukkan Input Yang Benar!!!")

def harga_barang():
    while True:
        harga = input("Masukkan harga Barang Per Biji: ")
        if harga.isdigit():
            return int(harga)
        else:
            print("Masukkan Input Yang Benar!!!")

def tambah_barang():
    id_barang = id()
    nama = input("Masukkan Nama Barang: ")
    banyak = banyak_barang()
    harga = harga_barang()
    total_harga = banyak * harga
    tanggal_barang =tanggal()
    kategori = daftar_kategori()

    barang = {
        "id": id_barang,
        "nama": nama,
        "banyak": banyak,
        "harga": harga,
        "total_harga":total_harga,
        "tanggal": tanggal_barang,
        "kategori":kategori
    }

    isi_tambah = {
        "id": id_barang,
        "nama": nama,
        "banyak": banyak,
        "harga": harga,
        "total_harga":total_harga,
        "tanggal": tanggal_barang,
        "kategori":kategori
    }

    daftar_barang.append(barang)
    laporan_tambah.append(isi_tambah)
    print(f"Barang {nama} Sudah Ditambahkan!!")

def tampilkan_barang():
    if daftar_barang:
        print("\n==Daftar Barang==")
        nomer = 1
        for barang in daftar_barang:
            print(f"\nDaftar Barang Ke-{nomer}")
            print(f"Nomer ID Barang: {barang['id']}")
            print(f"Nama Barang: {barang['nama']}")
            print(f"Banyaknya Barang: {barang['banyak']}")
            print(f"Harga Barang: Rp.{barang['total_harga']}")
            print(f"Ditambahkan Pada: {barang['tanggal']}")
            nomer += 1
    else:
        print("\n==Daftar Barang Tidak Ada==")
        return

def update_barang():
    cek = input("Masukkan ID Barang Yang Ingin Diupdate: ")
    for barang in daftar_barang:
        if barang["id"] == cek:
            print(f"Barang Ditemukan: {barang['nama']}")
            barang["id"] = id()
            barang["nama"] = input("Masukkan Nama Barang: ")
            barang["banyak"] = banyak_barang()
            barang["harga"] = harga_barang()
            barang["total_harga"] = barang["banyak"] * barang["harga"]
            barang["tanggal_barang"] =tanggal()
            print(f"Ditambahkan Pada: {barang['tanggal']}")
            print("Barang Berhasil Diupdate!!!")
            return
    print("Barang Tidak Ditemukan")

def hapus_barang():
    cek = input("Masukkan ID Barang Yang Ingin Dihapus: ")
    for barang in daftar_barang:
        if barang["id"] == cek:
            print(f"Barang Ditemukan: {barang['nama']}")
            daftar_barang.remove(barang)
            print("Barang Berhasil Dihapus!!!")
            return
    print("Barang Tidak Ditemukan")

def kelompokkan_barang():
    if daftar_barang :
        print("\nPilih Kategori untuk Ditampilkan:")
        kategori_barang = daftar_kategori()  
        barang_terpilih = []  
        for barang in daftar_barang:
            if barang["kategori"] == kategori_barang:
                barang_terpilih.append(barang)
    else:
        print("Daftar Barang Tidak Ada")
  
    if barang_terpilih:
        print(f"\n== Daftar Barang dalam Kategori: {kategori_barang} ==")
        nomer = 1
        for barang in barang_terpilih:
            print(f"{nomer}.Nama: {barang['nama']}\n ID: {barang['id']}\n Banyak: {barang['banyak']}\n Harga: {barang['harga']}")
            nomer += 1
    else:
        print(f"\nTidak ada barang dalam kategori {kategori_barang}.")

def total_barang():
    banyak_barang = 0
    for barang in daftar_barang:
        if "banyak" in barang:
            banyak_barang += barang["banyak"]
    print(f"Total Barang Saat Ini Adalah: {banyak_barang}")
    return

def total_harga():
    banyak_harga = 0
    for barang in daftar_barang:
        if "total_harga" in barang:
            banyak_harga += barang["total_harga"]
    print(f"Total Harga Saat Ini Adalah: Rp.{banyak_harga}")
    return

def total():
    print("\n==Total==")
    total_barang()
    total_harga()

def kurangi_stok():
    print("==Mengurangi stok barang berdasarkan ID.==")
    cek_id = input("\nMasukkan ID Barang yang Ingin Dikurangi: ")
    for barang in daftar_barang:
        if barang["id"] == cek_id:
            print(f"Barang Ditemukan: {barang['nama']} (Stok: {barang['banyak']})")
            jumlah_kurang = banyak_barang()
            if jumlah_kurang > barang["banyak"]:
                print("Stok tidak cukup untuk pengurangan!")
                return
            else:
                barang["banyak"] -= jumlah_kurang
                barang["total_harga"] = barang["banyak"] * barang["harga"]
                print(f"Stok barang '{barang['nama']}' berhasil dikurangi! Sisa stok: {barang['banyak']}")
                isi_kurang = {
                    "id":barang["id"],
                    "nama":barang["nama"],
                    "banyak":barang["banyak"],
                    "total_harga":jumlah_kurang*barang["harga"],
                    "tanggal":barang["tanggal"],
                    "kategori":barang["kategori"],
                }
                laporan_kurang.append(isi_kurang)
                return
        else:
            print("Barang tidak ditemukan!")

def Laporan_masuk():
    if laporan_tambah:
        nomer = 1
        print(f"\n==LAPORAN BARANG MASUK==")
        for barang in laporan_tambah:
            print(f"\nDaftar Barang Ke-{nomer}")
            print(f"Nomer ID Barang: {barang['id']}")
            print(f"Nama Barang: {barang['nama']}")
            print(f"Banyaknya Barang: {barang['banyak']}")
            print(f"Harga Barang: Rp.{barang['total_harga']}")
            print(f"Ditambahkan Pada: {barang['tanggal']}")
            print("-"*20)
            nomer += 1
    else:
        print(f"\n==LAPORAN BARANG MASUK==")
        print("Tidak Ada Barang Masuk.")
        return

            
def laporan_keluar():
    if laporan_kurang:
        nomer = 1
        print(f"\n==LAPORAN BARANG KELUAR==")
        for barang in laporan_kurang:
            print(f"\nDaftar Barang Ke-{nomer}")
            print(f"Nomer ID Barang: {barang['id']}")
            print(f"Nama Barang: {barang['nama']}")
            print(f"Banyaknya Barang: {barang['banyak']}")
            print(f"Harga Barang: Rp.{barang['total_harga']}")
            print(f"Ditambahkan Pada: {barang['tanggal']}")
            print("-"*20)
            nomer += 1
    else:
        print(f"\n==LAPORAN BARANG KELUAR==")
        print("Tidak Ada Barang Masuk.")
        return


def laporan():
    Laporan_masuk()
    laporan_keluar()

def main():
    while True:
        tampilan()
        pilihan = input("Pilih Menu (1-9): ")

        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            tampilkan_barang()
        elif pilihan == "3":
            update_barang()
        elif pilihan == "4":
            hapus_barang()
        elif pilihan == "5":
            kelompokkan_barang()
        elif pilihan == "6":
            total()
        elif pilihan == "7":
            kurangi_stok()
        elif pilihan == "8":
            laporan()
        elif pilihan == "9":
            print("\n==Program Telah Selesai!!!==")
            break
        else:
            print("Masukkan Pilihan Yang Benar BOSS!!!")

while True:
    print("\n===Login===")
    user = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    user_data = {user :"admin",
             password:"123"}  

    if user == user_data[user] and password == user_data[password]:
        print("Login Berhasil!!\n==Selamat Datang==")
        main()
        break
    else:
        print("Username Atau Password Salah!!!")

