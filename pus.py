class Buku:
    def __init__(self, judul, penulis, isbn):
        self.__judul = judul
        self.__penulis = penulis
        self.__isbn = isbn
        self.__tersedia = True
    
    def get_judul(self):
        return self.__judul
    
    def get_penulis(self):
        return self.__penulis
    
    def get_isbn(self):
        return self.__isbn
    
    def is_tersedia(self):
        return self.__tersedia
    
    def pinjam(self):
        if self.__tersedia:
            self.__tersedia = False
            return True
        return False
    
    def kembalikan(self):
        self.__tersedia = True


class Anggota:
    def __init__(self, nama, nomor_anggota, alamat):
        self.__nama = nama
        self.__nomor_anggota = nomor_anggota
        self.__alamat = alamat
        self.__buku_dipinjam = []
    
    def get_nama(self):
        return self.__nama
    
    def get_nomor_anggota(self):
        return self.__nomor_anggota
    
    def get_alamat(self):
        return self.__alamat
    
    def pinjam_buku(self, buku):
        if buku.pinjam():
            self.__buku_dipinjam.append(buku)
            return True
        return False
    
    def kembalikan_buku(self, buku):
        if buku in self.__buku_dipinjam:
            buku.kembalikan()
            self.__buku_dipinjam.remove(buku)
            return True
        return False
    
    def get_buku_dipinjam(self):
        return [buku.get_judul() for buku in self.__buku_dipinjam]


class Perpustakaan:
    def __init__(self):
        self.__daftar_buku = []
        self.__daftar_anggota = []
    
    def tambah_buku(self, buku):
        self.__daftar_buku.append(buku)
    
    def tambah_anggota(self, anggota):
        self.__daftar_anggota.append(anggota)
    
    def cari_buku(self, keyword):
        return [buku.get_judul() for buku in self.__daftar_buku if keyword.lower() in buku.get_judul().lower() or keyword.lower() in buku.get_penulis().lower()]
    
    def tampilkan_buku_tersedia(self):
        return [buku.get_judul() for buku in self.__daftar_buku if buku.is_tersedia()]

# Pengujian
perpustakaan = Perpustakaan()
b1 = Buku("Clean Code", "Robert C. Martin", "9780132350884")
b2 = Buku("The Pragmatic Programmer", "Andrew Hunt & David Thomas", "9780201616224")

perpustakaan.tambah_buku(b1)
perpustakaan.tambah_buku(b2)

anggota1 = Anggota("Ali", "A001", "Jl. Merdeka")
perpustakaan.tambah_anggota(anggota1)

print("Buku tersedia:", perpustakaan.tampilkan_buku_tersedia())
anggota1.pinjam_buku(b1)
print("Setelah peminjaman:", perpustakaan.tampilkan_buku_tersedia())
anggota1.kembalikan_buku(b1)
print("Setelah pengembalian:", perpustakaan.tampilkan_buku_tersedia())