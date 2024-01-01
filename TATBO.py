
class SpaceObject:
    def __init__(self, nama, umur, tinggi):
        self._nama = nama  
        self._umur = umur
        self._tinggi = tinggi

    def spacewalk(self):
        print(f"{self._nama} sedang melakukan spacewalk.")

    def info_tinggi(self):
        print(f"{self._nama} memiliki tinggi {self._tinggi} cm.")

    def umur_tahun_depan(self):
        return self._umur + 1

    def get_nama(self):  
        return self._nama



class LuarAngkasa(SpaceObject):
    def __init__(self, nama, massa, jarak_dari_matahari):
        super().__init__(nama, 0, 0)
        self.__massa = massa  
        self.__jarak_dari_matahari = jarak_dari_matahari

    def menjelajah(self):
        print(f"{self.get_nama()} sedang dijelajahi.")

    def tinggi(self): 
        print(f"{self.get_nama()} tidak memiliki tinggi karena bukan manusia, tapi jaraknya dari Matahari adalah {self.__jarak_dari_matahari} km.")

    def get_massa(self):  
        return self.__massa



class Roket(SpaceObject):
    def __init__(self, nama, tinggi, kecepatan_maks):
        super().__init__(nama, 0, tinggi)
        self.__kecepatan_maks = kecepatan_maks

    def meluncur(self):
        print(f"Roket {self.get_nama()} sedang meluncur dengan kecepatan maksimum {self.__kecepatan_maks} km/h.")

    def tambah_kecepatan(self, tambahan_kecepatan):
        self.__kecepatan_maks += tambahan_kecepatan

    def kecepatan_maksimal(self):
        return self.__kecepatan_maks == 40000

    def get_kecepatan_maks(self):  
        return self.__kecepatan_maks



class Bintang(LuarAngkasa):
    def __init__(self, nama, massa, jarak_dari_matahari, tipe):
        super().__init__(nama, massa, jarak_dari_matahari)
        self.__tipe = tipe  

    def tinggi(self): 
        print(f"{self.get_nama()} tidak memiliki tinggi karena bukan manusia, tapi merupakan bintang dengan tipe {self.__tipe}.")

    def get_tipe(self):  
        return self.__tipe



class Asteroid(LuarAngkasa):
    def __init__(self, nama, massa, jarak_dari_matahari, jenis_bahaya):
        super().__init__(nama, massa, jarak_dari_matahari)
        self.__jenis_bahaya = jenis_bahaya  

    def meteorit(self):
        print(f"Asteroid {self.get_nama()} sedang menjatuhkan meteorit. Hati-hati, jenis bahayanya adalah {self.__jenis_bahaya}.")

    def get_jenis_bahaya(self):  
        return self.__jenis_bahaya



objek_angkasa = [
    SpaceObject("Astronot 1", 35, 180),
    LuarAngkasa("Mars", 6.4171e23, 2.279e11),
    Roket("Apollo 11", 75, 40000),
    Bintang("Betelgeuse", 7.7e31, 640, "Raksasa Merah"),
    Asteroid("Ceres", 9.393e20, 4.45e8, "Potensial Berbahaya")
]


for objek in objek_angkasa:
    objek.spacewalk()
    objek.info_tinggi()

    if isinstance(objek, LuarAngkasa):
        objek.menjelajah()

    print("=" * 30)


roket_apollo = objek_angkasa[2]
roket_apollo.meluncur()


roket_apollo.tambah_kecepatan(5000)
print(f"Kecepatan roket setelah penambahan: {roket_apollo.get_kecepatan_maks()} km/h")


if roket_apollo.kecepatan_maksimal():
    print("Roket berada pada kecepatan maksimal.")
else:
    print("Roket belum mencapai kecepatan maksimal.")
