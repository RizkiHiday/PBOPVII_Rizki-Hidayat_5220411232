import mysql.connector

npm = "5220411232"

db = mysql.connector.connect(host="localhost", user="root", password="", database=npm) 
cursor = db.cursor()
import mysql.connector

class SpaceObject:
    def __init__(self, nama, umur, tinggi):
        self.nama = nama
        self.umur = umur
        self.tinggi = tinggi

    def display_info(self):
        print("Nama: {}".format(self.nama))
        print("Umur: {}".format(self.umur))
        print("Tinggi: {}".format(self.tinggi))


class PlanetObject(SpaceObject):
    def __init__(self, nama, jarak, massa):
        super().__init__(nama, None, None)  
        self.jarak = jarak
        self.massa = massa

    def display_info(self):
        super().display_info()
        print("Jarak dari Bintang: {}".format(self.jarak))
        print("Massa: {}".format(self.massa))


def insert_space_object(space_object):
    sql = "INSERT INTO space_objects (nama, umur, tinggi) VALUES (%s, %s, %s)"
    values = (space_object.nama, space_object.umur, space_object.tinggi)
    cursor.execute(sql, values)
    db.commit()
    print("{} berhasil ditambahkan".format(space_object.nama))


def show_space_objects():
    cursor.execute("SELECT * FROM space_objects")
    results = cursor.fetchall()

    for data in results:
        print(data)


def update_space_object(id, umur_baru):
    sql = "UPDATE space_objects SET umur=%s WHERE id=%s"
    values = (umur_baru, id)
    cursor.execute(sql, values)
    db.commit()
    print("Data berhasil diubah")


def delete_space_object(id):
    sql = "DELETE FROM space_objects WHERE id=%s"
    values = (id,)
    cursor.execute(sql, values)
    db.commit()
    print("Data berhasil dihapus")


def insert_planet_object(planet_object):
    sql = "INSERT INTO planet_objects (nama, jarak, massa) VALUES (%s, %s, %s)"
    values = (planet_object.nama, planet_object.jarak, planet_object.massa)
    cursor.execute(sql, values)
    db.commit()
    print("{} berhasil ditambahkan".format(planet_object.nama))


def show_planet_objects():
    cursor.execute("SELECT * FROM planet_objects")
    results = cursor.fetchall()

    for data in results:
        print(data)


def delete_planet_object(id):
    sql = "DELETE FROM planet_objects WHERE id=%s"
    values = (id,)
    cursor.execute(sql, values)
    db.commit()
    print("Data berhasil dihapus")


def show_menu():
    print("MENU".center(50, '='))
    print("1. Insert Data Space Object")
    print("2. Tampilkan Semua Data Space Object")
    print("3. Update Data Space Object")
    print("4. Hapus Data Space Object")
    print("5. Insert Data Planet Object")
    print("6. Tampilkan Semua Data Planet Object")
    print("7. Hapus Data Planet Object")
    print("0. Keluar")
    print("".center(50, '='))


def main_menu():
    pil = ""
    while pil != "0":
        show_menu()
        pil = input("Pilih menu> ")

        if pil == "1":
            nama = input("Masukkan nama: ")
            umur = int(input("Masukkan umur: "))
            tinggi = float(input("Masukkan tinggi: "))
            space_object = SpaceObject(nama, umur, tinggi)
            insert_space_object(space_object)
        elif pil == "2":
            show_space_objects()
        elif pil == "3":
            id_diupdate = input("Masukkan ID yang akan diupdate: ")
            umur_baru = input("Masukkan umur baru: ")
            update_space_object(id_diupdate, umur_baru)
        elif pil == "4":
            id_dihapus = input("Masukkan ID yang akan dihapus: ")
            delete_space_object(id_dihapus)
        elif pil == "5":
            nama_planet = input("Masukkan nama planet: ")
            jarak_planet = float(input("Masukkan jarak planet dari bintang: "))
            massa_planet = float(input("Masukkan massa planet: "))
            planet_object = PlanetObject(nama_planet, jarak_planet, massa_planet)
            insert_planet_object(planet_object)
        elif pil == "6":
            show_planet_objects()
        elif pil == "7":
            id_dihapus = input("Masukkan ID yang akan dihapus: ")
            delete_planet_object(id_dihapus)
        elif pil == "0":
            break


if __name__ == "__main__":
    db = mysql.connector.connect(host="localhost", user="root", password="", database=npm)
    cursor = db.cursor()
    main_menu()
    db.close()
