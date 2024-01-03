class Otomotif:
    def __init__(self, merk, tahunProduksi, harga):
        self.__merk = merk
        self.__tahunProduksi = tahunProduksi
        self.__harga = harga

    def Merk(self):
        return self.__merk

    def getTahunProduksi(self):
        return self.__tahunProduksi

    def getHarga(self):
        return self.__harga

    def setMerk(self, merk):
        self.__merk = merk

    def setTahunProduksi(self, tahun):
        self.__tahunProduksi = tahun

    def setHarga(self, harga):
        self.__harga = harga


class Mobil(Otomotif):
    def __init__(self, merk, tahunProduksi, harga, jumlahPintu, kapasitasMesin):
        super().__init__(merk, tahunProduksi, harga)
        self.__jumlahPintu = jumlahPintu
        self.__kapasitasMesin = kapasitasMesin

    def JumlahMobil(self):
        return self.__jumlahPintu

    def getKapasitasMesin(self):
        return self.__kapasitasMesin

    def setJumlahPintu(self, jumlah):
        self.__jumlahPintu = jumlah

    def setKapasitasMesin(self, kapasitas):
        self.__kapasitasMesin = kapasitas

#Operasi Aritmatika
    def hitungHargaPerMobil(self):
        return self.getHarga() * self.JumlahMobil()


class SUV(Mobil):
    def __init__(self, merk, tahunProduksi, harga, jumlahPintu, kapasitasMesin, model):
        super().__init__(merk, tahunProduksi, harga, jumlahPintu, kapasitasMesin)
        self.__model = model

    def Model(self):
        return self.__model

    def setModel(self, model):
        self.__model = model


# Inputan user/pengguna
merk = input("Masukkan merk mobil: ")
tahunProduksi = int(input("Masukkan tahun produksi: "))
harga = int(input("Masukkan harga: "))
jumlahPintu = int(input("Masukkan jumlah Mobil: "))
kapasitasMesin = int(input("Masukkan kapasitas mesin: "))
model = input("Masukkan model mobil: ")

# mengambil class yang ada di dalam objek yang bernama suv
suv = SUV(merk, tahunProduksi, harga, jumlahPintu, kapasitasMesin, model)

# Informaasi








































































print("\nInformasi Mobil:")
print("Merk:", suv.Merk())
print("Jumlah Mobil:", suv.JumlahMobil())
print("Harga Satu Mobil:", suv.hitungHargaPerMobil())
print("Model:", suv.Model())



