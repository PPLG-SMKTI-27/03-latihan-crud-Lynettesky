# data buku
books = [
    {"isbn":"9786237121144", "judul":"Kumpulan Solusi Pemrograman Python", "pengarang":"Budi Raharjo", "jumlah":6, "terpinjam":0},
    {"isbn":"9786231800718", "judul":"Dasar-Dasar Pengembangan Perangkat Lunak dan Gim Vol. 2", "pengarang":"Okta Purnawirawan", "jumlah":15, "terpinjam":0},
    {"isbn":"9786026163905", "judul":"Analisis dan Perancangan Sistem Informasi", "pengarang":"Adi Sulistyo Nugroho", "jumlah":2, "terpinjam":1},
    {"isbn":"9786022912828", "judul":"Animal Farm", "pengarang":"George Orwell", "jumlah":4, "terpinjam":0}
]

# data peminjaman
records = [
    {"isbn":"9786022912828", "status":"Selesai", "tanggal_pinjam":"2025-03-21", "tanggal_kembali":"2025-03-28"},
    {"isbn":"9786026163905", "status":"Belum", "tanggal_pinjam":"2025-07-22", "tanggal_kembali":""}
]

def tampilkan_data():
    print("\n== Daftar Barang ==")
    for i in range(len(books)):
        print(f"{i+1}.isbn: {books[i]['isbn']} - judul: {books[i]['judul']} - Jumlah: {books[i]['jumlah']} - terpinjam: {books[i]['terpinjam']}")
    menu()
def tambah_data():
    isbn = int(input("Masukkan no isbn: "))
    judul = input("Masukkan Judul Buku: ")
    pengarang = input("Masukkan nama pengarang: ")
    jumlah = int(input("Masukkan jumlah barang: "))
    terpinjam = int(input("masukkan jumlah yang terpinjam:"))
    buku_baru = {"isbn": isbn, "judul": judul, "Pengarang": pengarang, "jumlah": jumlah, "terpinjam": terpinjam}
    books.append(buku_baru)
    print("Buku berhasil ditambahkan!\n")

def edit_data():
    isbn = int(input("Masukkan no Isbn: "))
    judul = input("Masukkan judul buku: ")
    pengarang = input("Masukkan nama pengarang: ")
    jumlah = int(input("Masukkan jumlah buku: "))
    terpinjam = int(input("masukkan jumlah yang terpinjam:"))
    data_ubah = ({"isbn": isbn, "judul": judul, "Pengarang": pengarang, "jumlah": jumlah, "terpinjam": terpinjam})

    indeks_ubah = int(input("masukkan no data yang ingin diubah: "))-1
    books[indeks_ubah] = data_ubah

    print("Data berhasil diubah!")

def hapus_data():
    indeks_hapus = int(input("Masukkan nomor data yang dihapus: "))-1
    del books[indeks_hapus]
    menu()

def tampilkan_peminjaman():
    for i in range(len(records)):
        print(f"{i+1}. isbn: {records[i]['isbn']} - status: {records[i]['status']} - tanggal_pinjam: {records[i]['tanggal_pinjam']} - tanggal_kembali: {records[i]['tanggal_kembali']}")

def tampilkan_belum():
    if not records:
        print("Tidak ada peminjaman")
        return
    
    for record in records:
        if record['status'] == "Belum":
            print(f"ISBN: {record['isbn']}, tanggal pinjam: {record['tanggal_pinjam']} tanggal pengembalian: {record['tanggal_kembali']}")

def peminjaman():
    isbn = input("Masukkan ISBN buku yang ingin dipinjam: ")
    for book in books:
        if book['isbn'] == isbn:
            if book['jumlah'] > book['terpinjam']:
                book['terpinjam'] += 1
                records.append({"isbn": isbn, "status": "Belum", "tanggal_pinjam": "2025-03-21", "tanggal_kembali": ""})
                print("Buku berhasil dipinjam.")
            else:
                print("Buku sudah habis dipinjam.")
            return
    print("Buku dengan ISBN ini tidak ditemukan.")

def pengembalian():
    isbn = input("Masukkan ISBN buku yang ingin dikembalikan: ")
    balik_buku = input("tanggal buku pas mau di kembalikan:")
    for book in books:
        if book['isbn'] == isbn:
            if book['terpinjam'] > 0:
                book['terpinjam'] -= 1
                for record in records:
                    if record['isbn'] == isbn and record['status'] == "Belum":
                        record['status'] = "Selesai"
                        record['tanggal_kembali'] = balik_buku
                        break
                print("Buku berhasil dikembalikan.")
            else:
                print("Buku ini tidak sedang dipinjam.")
            return
    print("Buku dengan ISBN ini tidak ditemukan.")



def menu():
    while ...:
        print("---=== MENU ===---")
        print("[1] Tampilkan Data")
        print("[2] Tambah Data")
        print("[3] Edit Data")
        print("[4] Hapus Data")
        print("------------------")
        print("[5] Tampilkan Semua Peminjaman")
        print("[6] Tampilkan Peminjaman Belum Kembali")
        print("[7] Peminjaman")
        print("[8] Pengembalian")
        print("[X] Keluar")

        pilihan = input("Masukkan pilihan menu (1-8 atau x): ")
        
        match pilihan:
            case "1":
                print("masuk ke menu Tampilkan Data")
                tampilkan_data()

            case "2":
                print("masuk ke menu Tambah Data")
                tambah_data()

            case "3":
                print("masuk ke menu Ubah Data")
                edit_data()

            case "4":
                print("hapus data Data Buku")
                hapus_data()

            case "5":
                print("Masuk ke menu Tampilkan Semua Peminjaman")
                tampilkan_peminjaman()

            case "6":
                print("Tampilkan Peminjaman Belum Kembali")
                tampilkan_belum()

            case "7":
                print("Masuk ke menu Peminjaman")
                peminjaman()

            case "8":
                print("Masuk ke menu Pengembalian")
                pengembalian()
            
            case "x":
                print("Keluar dari program")
                exit()
                break

menu()
    