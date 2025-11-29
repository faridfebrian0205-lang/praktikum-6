# Dictionary untuk menyimpan data mahasiswa
data_mahasiswa = {}

# Fungsi untuk menambah data
def tambah():
    nama = input("Masukkan nama: ")
    nilai = input("Masukkan nilai: ")
    data_mahasiswa[nama] = nilai
    print(f"Data untuk {nama} berhasil ditambahkan.\n")

# Fungsi untuk menampilkan data
def tampilkan():
    if data_mahasiswa:
        print("Daftar Nilai Mahasiswa:")
        for nama, nilai in data_mahasiswa.items():
            print(f"- {nama}: {nilai}")
    else:
        print("Tidak ada data mahasiswa.")
    print()

# Fungsi untuk menghapus data berdasarkan nama
def hapus(nama):
    if nama in data_mahasiswa:
        del data_mahasiswa[nama]
        print(f"Data {nama} berhasil dihapus.\n")
    else:
        print(f"Data {nama} tidak ditemukan.\n")

# Fungsi untuk mengubah data berdasarkan nama
def ubah(nama):
    if nama in data_mahasiswa:
        nilai_baru = input(f"Masukkan nilai baru untuk {nama}: ")
        data_mahasiswa[nama] = nilai_baru
        print(f"Data {nama} berhasil diubah.\n")
    else:
        print(f"Data {nama} tidak ditemukan.\n")

# Program utama
while True:
    print("Menu:")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar")

    pilihan = input("Pilih menu (1/2/3/4/5): ")

    if pilihan == "1":
        tambah()
    elif pilihan == "2":
        tampilkan()
    elif pilihan == "3":
        nama = input("Masukkan nama yang akan dihapus: ")
        hapus(nama)
    elif pilihan == "4":
        nama = input("Masukkan nama yang akan diubah: ")
        ubah(nama)
    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.\n")
