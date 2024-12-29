class AkilliEv:
    def init(self):
        self.isiklar = {}
        self.termostat = {"sicaklik": 22, "mod": "otomatik"}  # Varsayilan 22°C
        self.guvenlik_sistemi = {"durum": "devre dişi"}
        self.cihazlar = {}

    # Işık yönetimi
    def isik_ekle(self, oda):
        self.isiklar[oda] = False
        print(f"{oda} odasina işik eklendi.")

    def isik_kontrol(self, oda, durum):
        if oda in self.isiklar:
            self.isiklar[oda] = durum
            print(f"{oda} odasindaki işik {'açildi' if durum else 'kapandi'}.")
        else:
            print(f"{oda} odasinda işik bulunamadi.")

    # Termostat yönetimi
    def sicaklik_ayarla(self, sicaklik):
        self.termostat["sicaklik"] = sicaklik
        print(f"Termostat {sicaklik}°C'ye ayarlandi.")

    def mod_ayarla(self, mod):
        if mod in ["otomatik", "soğutma", "isitma", "kapali"]:
            self.termostat["mod"] = mod
            print(f"Termostat modu {mod} olarak ayarlandi.")
        else:
            print("Geçersiz mod. 'otomatik', 'soğutma', 'isitma' veya 'kapali' kullanabilirsiniz.")

    # Güvenlik sistemi yönetimi
    def guvenlik_etkinlestir(self):
        self.guvenlik_sistemi["durum"] = "etkin"
        print("Güvenlik sistemi etkinleştirildi.")

    def guvenlik_devre_disibirak(self):
        self.guvenlik_sistemi["durum"] = "devre dişi"
        print("Güvenlik sistemi devre dişi birakildi.")

    # Cihaz yönetimi
    def cihaz_ekle(self, ad):
        self.cihazlar[ad] = False
        print(f"{ad} cihazi eklendi.")

    def cihaz_kontrol(self, ad, durum):
        if ad in self.cihazlar:
            self.cihazlar[ad] = durum
            print(f"{ad} {'açildi' if durum else 'kapandi'}.")
        else:
            print(f"{ad} adli cihaz bulunamadi.")

    # Sistem durumu gösterimi
    def durum(self):
        print("\n--- Akilli Ev Durumu ---")
        print("Işiklar:", self.isiklar)
        print("Termostat:", self.termostat)
        print("Güvenlik Sistemi:", self.guvenlik_sistemi["durum"])
        print("Cihazlar:", self.cihazlar)
        print("--------------------------\n")


# Örnek Kullanım
ev = AkilliEv()

# Işık yönetimi
ev.isik_ekle("Oturma Odasi")
ev.isik_kontrol("Oturma Odasi", True)
ev.isik_kontrol("Yatak Odasi", False)

# Termostat yönetimi
ev.sicaklik_ayarla(24)
ev.mod_ayarla("soğutma")

# Güvenlik sistemi yönetimi
ev.guvenlik_etkinlestir()
ev.guvenlik_devre_disibirak()

# Cihaz yönetimi
ev.cihaz_ekle("Çamaşir Makinesi")
ev.cihaz_kontrol("Çamaşir Makinesi", True)

# Sistem durumu gösterimi
ev.durum()