# Kelas dasar Produk
class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok
    
    def tampilkanInfo(self):
        return f"Nama: {self.nama}, Harga: {self.harga}, Stok: {self.stok}"

# Kelas turunan Buku
class Buku(Produk):
    def __init__(self, nama, harga, stok, penulis, penerbit):
        super().__init__(nama, harga, stok)
        self.penulis = penulis
        self.penerbit = penerbit
    
    def tampilkanInfo(self):
        return super().tampilkanInfo() + f", Penulis: {self.penulis}, Penerbit: {self.penerbit}"

# Kelas turunan Elektronik
class Elektronik(Produk):
    def __init__(self, nama, harga, stok, merek, garansi):
        super().__init__(nama, harga, stok)
        self.merek = merek
        self.garansi = garansi
    
    def tampilkanInfo(self):
        return super().tampilkanInfo() + f", Merek: {self.merek}, Garansi: {self.garansi} tahun"

# Kelas turunan Pakaian
class Pakaian(Produk):
    def __init__(self, nama, harga, stok, ukuran, warna):
        super().__init__(nama, harga, stok)
        self.ukuran = ukuran
        self.warna = warna
    
    def tampilkanInfo(self):
        return super().tampilkanInfo() + f", Ukuran: {self.ukuran}, Warna: {self.warna}"

# Kelas Inventaris
class Inventaris:
    def __init__(self):
        self.daftar_produk = []
    
    def tambahProduk(self, produk):
        self.daftar_produk.append(produk)
    
    def hapusProduk(self, nama):
        self.daftar_produk = [produk for produk in self.daftar_produk if produk.nama != nama]
    
    def cariProduk(self, nama):
        for produk in self.daftar_produk:
            if produk.nama.lower() == nama.lower():
                return produk.tampilkanInfo()
        return "Produk tidak ditemukan"
    
    def tampilkanSemuaProduk(self):
        if not self.daftar_produk:
            return "Inventaris kosong"
        return "\n".join([produk.tampilkanInfo() for produk in self.daftar_produk])

# Contoh Penggunaan
if __name__ == "__main__":
    inventaris = Inventaris()
    
    # Menambahkan produk
    buku1 = Buku("Python Basics", 100000, 10, "Guido van Rossum", "TechBooks")
    elektronik1 = Elektronik("Laptop", 7000000, 5, "Asus", 2)
    pakaian1 = Pakaian("Kaos", 150000, 20, "L", "Hitam")
    
    inventaris.tambahProduk(buku1)
    inventaris.tambahProduk(elektronik1)
    inventaris.tambahProduk(pakaian1)
    
    # Menampilkan semua produk
    print("\nDaftar Produk:")
    print(inventaris.tampilkanSemuaProduk())
    
    # Mencari produk
    print("\nCari Produk:")
    print(inventaris.cariProduk("Laptop"))
    
    # Menghapus produk
    inventaris.hapusProduk("Kaos")
    print("\nDaftar Produk setelah penghapusan:")
    print(inventaris.tampilkanSemuaProduk())
