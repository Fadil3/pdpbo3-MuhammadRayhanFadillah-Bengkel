from kendaraan import Kendaraan

class Motor(Kendaraan):
    def __init__(self, pemilik, layanan,jenis_transmisi,bahan_bakar):
        super().__init__(jenis_transmisi, bahan_bakar)
        self.pemilik = pemilik
        self.layanan = layanan
    
    def get_pemilik(self):
        return self.pemilik

    def get_layanan(self):
        return self.layanan
