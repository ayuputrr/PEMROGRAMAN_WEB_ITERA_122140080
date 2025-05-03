from abc import ABC, abstractmethod

print("=== Selamat datang di Perpustakaan Werebook ===")
class ItemPerpustakaan(ABC):
    def __init__(self, kode, judul):
        self._kode = kode           
        self._judul = judul         

    @abstractmethod
    def tampilkan_info(self):
        pass


    @property
    def judul(self):
        return self._judul

    @judul.setter
    def judul(self, nilai):
        if nilai:
            self._judul = nilai
        else:
            print("Judul tidak boleh kosong.")

    def get_kode(self):
        return self._kode


class Buku(ItemPerpustakaan):
    def __init__(self, kode, judul, penulis):
        super().__init__(kode, judul)
        self.__penulis = penulis  

 
    def tampilkan_info(self):
        print(f"[Buku] Kode: {self._kode}, Judul: {self._judul}, Penulis: {self.__penulis}")


class Majalah(ItemPerpustakaan):
    def __init__(self, kode, judul, edisi):
        super().__init__(kode, judul)
        self.__edisi = edisi  

   
    def tampilkan_info(self):
        print(f"[Majalah] Kode: {self._kode}, Judul: {self._judul}, Edisi: {self.__edisi}")


class Perpustakaan:
    def __init__(self):
        self._koleksi = [] 

    def tambah_item(self, item):
        self._koleksi.append(item)
        print(f"Item '{item.judul}' berhasil ditambahkan.")

    def tampilkan_koleksi(self):
        if not self._koleksi:
            print("Belum ada koleksi.")
            return
        print("\nDaftar Koleksi:")
        for item in self._koleksi:
            item.tampilkan_info()

    def cari_item(self, kata_kunci):
        print(f"\nHasil pencarian untuk '{kata_kunci}':")
        ditemukan = False
        for item in self._koleksi:
            if kata_kunci.lower() in item.judul.lower() or kata_kunci.lower() in item.get_kode().lower():
                item.tampilkan_info()
                ditemukan = True
        if tidak_ditemukan := not ditemukan:
            print("Item tidak ditemukan.")

def menu():
    perpustakaan = Perpustakaan()
    while True:
        print("\n=== Menu Perpustakaan ===")
        print("1. Tambah Buku")
        print("2. Tambah Majalah")
        print("3. Tampilkan Koleksi")
        print("4. Cari Item")
        print("5. Keluar")
        pilihan = input("Pilih (1-5): ")

        if pilihan == "1":
            kode = input("Masukkan kode buku: ")
            judul = input("Masukkan judul buku: ")
            penulis = input("Masukkan nama penulis: ")
            buku = Buku(kode, judul, penulis)
            perpustakaan.tambah_item(buku)
        elif pilihan == "2":
            kode = input("Masukkan kode majalah: ")
            judul = input("Masukkan judul majalah: ")
            edisi = input("Masukkan edisi majalah: ")
            majalah = Majalah(kode, judul, edisi)
            perpustakaan.tambah_item(majalah)
        elif pilihan == "3":
            perpustakaan.tampilkan_koleksi()
        elif pilihan == "4":
            kata_kunci = input("Masukkan judul atau kode: ")
            perpustakaan.cari_item(kata_kunci)
        elif pilihan == "5":
            print("Terima kasih Telah Mengunjungi Perpustakaan Werebook!!!.")
            break
        else:
            print("Pilihan tidak valid.")
menu()

