# Створіть клас для опису товару (припустимо, це заділ для інтернет-магазину).
# Як поля товару можете використовувати значення ціни, опис, габарити товару.
# Створіть пару екземплярів вашого класу та протестуйте їхню роботу. Створіть
# клас "Покупець". Як поля можна використовувати прізвище, ім'я, по батькові,
# мобільний телефон і т.д. Створіть клас "Замовлення". Замовлення може містити
# кілька товарів, причому кількість кожного з товарів може бути різною.
# Замовлення має бути "підв'язане" до користувача, який його здійснив.
# Реалізуйте метод обчислення сумарної вартості замовлення. Визначте метод
# str() для коректного виведення інформації про це замовлення.

class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name} - {self.price} грн, {self.description}, Розміри: {self.dimensions}"


class User:
    def __init__(self, surname, name, patronymic, phone):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone = phone

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}, Телефон: {self.phone}"


class Purchase:
    def __init__(self, customer, address):
        self.customer = customer
        self.address = address
        self.products = {}

    def add_product(self, product, quantity):
        if quantity <= 0:
            raise ValueError("Кількість товару має бути додатною")
        self.products[product] = self.products.get(product, 0) + quantity

    def total_price(self):
        return sum(product.price * quantity for product, quantity in self.products.items())

    def __str__(self):
        result = f"Замовлення\nПокупець: {self.customer}\nАдреса: {self.address}\nТовари:\n"

        for product, quantity in self.products.items():
            result += f"{product.name} - {quantity} шт. x {product.price} грн = {product.price * quantity} грн\n"

        result += f"Загальна вартість: {self.total_price()} грн"
        return result


lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40
