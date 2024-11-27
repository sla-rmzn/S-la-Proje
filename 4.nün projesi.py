from datetime import datetime
import os


class Product:
    def _init_(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        print(f"Ürün oluşturuldu: {self.name}, Tarih: {datetime.now()}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not (3 <= len(value) <= 8):
            raise ValueError("Ürün ismi 3 ile 8 karakter arasında olmalıdır.")
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Ürün fiyatı negatif olamaz.")
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 1:
            raise ValueError("Ürün adedi 1'den küçük olamaz.")
        self._quantity = value

    def get_total_price(self):
        return self.price * self.quantity

    def _str_(self):
        return f"Ürün: {self.name}, Fiyat: {self.price}, Adet: {self.quantity}, Toplam: {self.get_total_price()}"


class ProductHelper:
    @staticmethod
    def create_item_from_text(file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file_path} bulunamadı.")
        
        product_list = []
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 3:
                    try:
                        name = data[0].strip()
                        price = float(data[1].strip())
                        quantity = int(data[2].strip())
                        product = Product(name, price, quantity)
                        product_list.append(product)
                    except (ValueError, IndexError) as e:
                        print(f"Hatalı satır atlandı: {line} -> {e}")
        return product_list

    @staticmethod
    def get_total_balance(product_list):
        total = sum(product.get_total_price() for product in product_list)
        return total * 1.20  # %20 KDV ekleniyor

    @staticmethod
    def create_product_file(file_path):
        products = [
            "Elma, 5.0, 10",
            "Armut, 4.5, 15",
            "Çilek, 20.0, 5",
            "Portakal, 6.0, 8",
            "Hatalıveri",
            "Karpuz, -10, 1"
        ]
        with open(file_path, "w", encoding="utf-8") as file:
            file.write("\n".join(products))
        print(f"{file_path} dosyası başarıyla oluşturuldu.")


def main():
    file_path = "product.txt"
    
    # Dosyayı oluştur
    ProductHelper.create_product_file(file_path)
    
    try:
        # Ürünleri dosyadan yükle
        products = ProductHelper.create_item_from_text(file_path)
        print("\nÜrünler başarıyla yüklendi:")
        for product in products:
            print(product)
        
        # Toplam ödeme miktarını hesapla
        total_balance = ProductHelper.get_total_balance(products)
        print(f"\nToplam ödeme miktarı (KDV dahil): {total_balance:.2f} TL")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")


if _name_ == "_main_":
    main()