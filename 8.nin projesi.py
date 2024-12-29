class Account:
    accounts = []  # Tüm hesapları saklayan static liste

    def _init_(self, account_number, owner, balance):
        self.__account_number = account_number  # Private düzeyde hesap numarası
        self.__owner = owner  # Private düzeyde hesap sahibi
        self.__balance = balance  # Private düzeyde bakiye
        Account.accounts.append(self)  # Hesap nesnesini static listeye ekleme

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} TL yatırıldı. Yeni bakiye: {self.__balance} TL")
            Bank.track_transaction(f"{self._owner} ({self._account_number}) hesabına {amount} TL yatırıldı.")
        else:
            print("Geçersiz tutar. Pozitif bir miktar girin.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Yetersiz bakiye.")
        elif amount > 0:
            self.__balance -= amount
            print(f"{amount} TL çekildi. Kalan bakiye: {self.__balance} TL")
            Bank.track_transaction(f"{self._owner} ({self._account_number}) hesabından {amount} TL çekildi.")
        else:
            print("Geçersiz tutar. Pozitif bir miktar girin.")

    def view_balance(self):
        print(f"Hesap Sahibi: {self.__owner}")
        print(f"Hesap Numarası: {self.__account_number}")
        print(f"Bakiye: {self.__balance} TL")


class Bank:
    transaction_history = []  # Tüm hesap işlemlerini saklayan static liste

    @staticmethod
    def display_bank_info():
        print("\n--- Banka Bilgileri ---")
        print("Banka Adı: Python Bank")
        print("Toplam Hesap Sayısı:", len(Account.accounts))

    @staticmethod
    def track_transaction(description):
        Bank.transaction_history.append(description)

    @staticmethod
    def display_transaction_history():
        print("\n--- İşlem Geçmişi ---")
        for transaction in Bank.transaction_history:
            print(transaction)


# Örnek Kullanım
if _name_ == "_main_":
    # Hesaplar oluşturuluyor
    account1 = Account("123456", "Ece Kara", 1000)
    account2 = Account("654321", "Aysun Kaya", 2000)

    # Hesap işlemleri
    account1.view_balance()
    account1.deposit(500)
    account1.withdraw(300)
    account1.withdraw(1500)  # Yetersiz bakiye kontrolü

    account2.view_balance()
    account2.withdraw(1000)

    # Banka bilgileri ve işlem geçmişi
    Bank.display_bank_info()
    Bank.display_transaction_history()