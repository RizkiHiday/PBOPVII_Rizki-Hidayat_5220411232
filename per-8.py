class PerpusItem:
    def __init__(self, judul, subjek):
        self.judul = judul
        self.subjek = subjek

    def lokasiPenyimpanan(self):
        pass

    def info(self):
        print("Judul:",self.judul)
        print("Subjek:",self.subjek)


class Buku(PerpusItem):
    def __init__(self, judul, subjek, ISBN, pengarangs, jmlHal, ukuran):
        super().__init__(judul, subjek)
        self.ISBN = ISBN
        self.pengarangs = pengarangs
        self.jmlHal = jmlHal
        self.ukuran = ukuran

    def info(self):
        super().info()
        print("ISBN:",self.ISBN)
        print("Pengarang:",self.pengarangs)
        print("Jumlah Halaman:",self.jmlHal)
        print("Ukuran:", self.ukuran)


class Majalah(PerpusItem):
    def __init__(self, judul, subjek, volume, issue):
        super().__init__(judul, subjek)
        self.volume = volume
        self.issue = issue

    def info(self):
        super().info()
        print("Volume:",self.volume)
        print("Issue:",self.issue)


class DVD(PerpusItem):
    def __init__(self, judul, subjek, actor, genre):
        super().__init__(judul, subjek)
        self.actor = actor
        self.genre = genre

    def info(self):
        super().info()
        print("Aktor:",self.actor)
        print("Genre:",self.genre)


class Katalog:
    def cari(self):
        pass


class Pengarang:
    def __init__(self, nama):
        self.nama = nama

    def info(self):
        print("Nama Pengarang:",self.nama)

    def cari(self):
        pass

buku = Buku(judul="Om Anton", subjek="Hiburan", ISBN="20202209", pengarangs="Kuncoro +", jmlHal="100", ukuran="A5")
buku.info()
