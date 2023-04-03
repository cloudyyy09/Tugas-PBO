class Musisi:
    def __init__(self, nama, band):
        self.nama = nama
        self.band = band
    
    def lagu(self, lagu):
        print(f"{self.nama} dari band {self.band} memiliki lagu {lagu}")
        
kucing = Musisi("Arman", "gigi")
anjing = Musisi("kaka", "slank")

kucing.lagu("Panas") 
anjing.lagu("Ku tak bisa") 