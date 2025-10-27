class Kendaraan(object):
    jenis = None

    def _init_(self, jenis):
        self.jenis = jenis

    def berjalan(self):
        print('{} berjalan di jalan raya.'.format(self.jenis))

class KendaraanListrik(Kendaraan):
    jenis = None
    kapasitas_baterai = None

    def _init_(self, jenis):
        self.jenis = jenis

    def berjalan(self):
        print('{} berjalan secara otomatis (listrik).'.format(self.jenis))

    def set_kapasitas_baterai(self, kapasitas):
        self.kapasitas_baterai = kapasitas

# Contoh penggunaan
mobil_listrik = KendaraanListrik('Tesla Model 3')
mobil_listrik.set_kapasitas_baterai('75 kWh')
mobil_listrik.berjalan()  # Output: Tesla Model 3 berjalan secara otomatis (listrik).

motor_listrik = KendaraanListrik('Gesits')
motor_listrik.set_kapasitas_baterai('5 kWh')
motor_listrik.berjalan()  # Output: Gesits berjalan secara otomatis (listrik).