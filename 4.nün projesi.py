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
        with open(file_path, "r") as file:
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
        total = sum([product.get_total_price() for product in product_list])
        return total * 1.20  # %20 KDV ekleniyor


def main():
    file_path = "product.txt"
    
    try:
        products = ProductHelper.create_item_from_text(file_path)
        print("Ürünler başarıyla yüklendi:")
        for product in products:
            print(product)
        
        total_balance = ProductHelper.get_total_balance(products)
        print(f"Toplam ödeme miktarı (KDV dahil): {total_balance:.2f} TL")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")


if _name_ == "_main_":
    main()