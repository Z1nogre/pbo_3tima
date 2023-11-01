# edytdgfd
import mysql.connector
# buat connection ke dalam database mysqlnya
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="obat_pet"
)

#VVVVV di infokan kalau terkonek ke dalam database mysql
if connection.is_connected():
    print("Connected to the MySQL database")
cursor = connection.cursor()

#class buat supps
class Supplement:
    def __init__(self):
        self.obat = []

    def tambahkan_obat(self, obat):
        self.obat.append(obat)

    def dapatkan_obat(self):
        return self.obat

    def temukan_obat(self, nama):
        for obat in self.obat:
            if obat.nama == nama:
                return obat
        return None
#class buat obatpet
class ObatPet:
    def __init__(self, id, nama, harga, deskripsi):
        self.id = id
        self.nama = nama
        self.harga = harga
        self.deskripsi = deskripsi

    def get_id(self):
        return self.id

    def get_nama(self):
        return self.nama

    def get_harga(self):
        return self.harga

    def get_deskripsi(self):
        return self.deskripsi

# buat toko obatnya
toko_obat_pet = Supplement() 

# ambil data dari database dan isi penyimpanan
query = "SELECT * FROM supps"
cursor.execute(query)
for (id, nama, harga, deskripsi) in cursor:
    toko_obat_pet.tambahkan_obat(ObatPet(id, nama, harga, deskripsi))

# fungsi untuk memasukkan data baru ke dalam databasenya
def insert_obat(nama, harga, deskripsi):
    query = ("INSERT INTO supps(Nama_obat, Harga_obat, Deskripsi_obat) "               #select udpate insert dan delete mirip2 seperti ini
             "VALUES (%s, %s, %s)")                                                    #notes: nomor ID saya incrament primary key jd gk perlu isi
    data = (nama, harga, deskripsi)
    cursor.execute(query, data)
    connection.commit()

# fungsi untuk mengupdate data yang sudah ada dalam databasenya
def update_obat(obat_nama, harga_baru):
    query = "UPDATE `supps` SET `Harga_obat` = %s WHERE `Nama_obat` = %s"
    data = (harga_baru, obat_nama)
    cursor.execute(query, data)
    connection.commit()
    print("Harga obat berhasil diperbarui.")

# fungsi untuk menghapus data dalam databasenya
def delete_obat(id):
    query = "DELETE FROM `supps` WHERE `ID` = %s"
    data = (id,)
    cursor.execute(query, data)
    connection.commit()
    print("Itemnya telah di remove dari shelf") 

# loop interaktif VVV
while True:
    input_pengguna = input("Apa yang ingin anda lakukan? \n(1) Lihat obat, (2) Beli obat, (3) Keluar, (4) Tambah Stok baru, (5) Update Harga, (6) Remove Obat\n")
    if input_pengguna == "1":
        print("Ini obat-obat yang dalam stok:")
        for obat in toko_obat_pet.dapatkan_obat():
            print(obat.get_nama(), obat.get_harga(), obat.get_deskripsi())
    elif input_pengguna == "2": #kode untuk membeli obat pet
        print("Obat apa yang ingin anda beli?")
        nama_obat = input()
        obat = toko_obat_pet.temukan_obat(nama_obat)
        if obat is None:
            print("Maaf, obat itu tidak dalam stok.")
        else:
            print("Anda membeli {} seharga Rp{}.".format(obat.get_nama(), obat.get_harga()))
            print("Apakah anda ingin mengkonfirmasi pembelian anda? (y/n)")
            input_pengguna = input()
            if input_pengguna == "y":
                print("Terima kasih atas pembelian anda!")
            else:
                print("Cari lagi yang anda perlu")
    elif input_pengguna == "4": ##INSERT /// kode untuk menambahkan stok obat pet baru
        print("Mau menambah stock apa?")
        n = input("Nama Obat: ")
        h = input("Harga Obat: ")
        d = input("Deskripsi Obat: ")
        insert_obat(n, h, d)
        print("Makasih dengan stocknya, akan segera di kirim ke dalam databasenya.")
        #^^^^input insert nama, harga, dan deskripsi. harga harus string yang hanya punya angka
        #run insert_obat() input_program
    elif input_pengguna == "5": ##UPDATE /// kode untuk memperbarui harga obat pet
        print("Mau update harga apa? (Nama_obat)")
        for obat in toko_obat_pet.dapatkan_obat():
            obat_nama = input("Masukkan ID obat yang anda ingin di update: ")
            harga_baru = input("Masukkan harga baru: ")
            update_obat(obat_nama, harga_baru)
        #^^^^input untuk update
    elif input_pengguna == "6": ##DELETE /// kode untuk menghapus obat pet dari databasenya
        print("Item apa yang anda mau di remove?? (ID)") 
        for obat in toko_obat_pet.dapatkan_obat():
            id_obat = input()
            delete_obat(id_obat)
        #input untuk delete
    else:
        print("Come again soon!")
        break
cursor.close() # tutup cursor dan koneksio database
connection.close()