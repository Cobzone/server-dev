class Customer:
    def __init__(self, id, last_name, first_name, middle_name, address, credit_card_number, bank_account_number):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.address = address
        self.credit_card_number = credit_card_number
        self.bank_account_number = bank_account_number

    # Геттеры
    def get_id(self):
        return self.id

    def get_last_name(self):
        return self.last_name

    def get_first_name(self):
        return self.first_name

    def get_middle_name(self):
        return self.middle_name

    def get_address(self):
        return self.address

    def get_credit_card_number(self):
        return self.credit_card_number

    def get_bank_account_number(self):
        return self.bank_account_number

    # Сеттеры
    def set_id(self, id):
        self.id = id

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_middle_name(self, middle_name):
        self.middle_name = middle_name

    def set_address(self, address):
        self.address = address

    def set_credit_card_number(self, credit_card_number):
        self.credit_card_number = credit_card_number

    def set_bank_account_number(self, bank_account_number):
        self.bank_account_number = bank_account_number

    def __str__(self):
        return f"Customer [id={self.id}, {self.last_name} {self.first_name} {self.middle_name}, Адрес: {self.address}, Номер кредитной карты: {self.credit_card_number}, Номер счёта: {self.bank_account_number}]"

    def hash_code(self):
        return self.id


customers = [
    Customer(1, "Асанов", "Осман", "Эрпанович", "Евпатория", "1234567890123456", "111111"),
    Customer(2, "Сейтумеров", "Эдем", "Рустемович", "Кировское", "9876543210987654", "222222"),
    Customer(3, "Рудов", "Илья", "Сергеевич", "ГРЭС", "1111222233334444", "333333"),
    Customer(4, "Минзатов", "Эмран", "Серверович", "Старый Крым", "5555666677778888", "444444"),
    Customer(5, "Бекиров", "Дилявер", "Энверович", "Симферополь", "4444555566667777", "555555")
]

# Сортировка покупателей по фамилии
print("Список покупателей в алфавитном порядке:")
for customer in sorted(customers, key=lambda c: c.get_last_name()):
    print(customer)

def get_customers_by_card_range(min_card_number, max_card_number):
    return [customer for customer in customers if min_card_number <= customer.get_credit_card_number() <= max_card_number]

min_card_number = "4000000000000000"
max_card_number = "6000000000000000"

print(f"\nСписок покупателей с номерами кредитных карт в интервале от {min_card_number} до {max_card_number}:")
for customer in get_customers_by_card_range(min_card_number, max_card_number):
    print(customer)
