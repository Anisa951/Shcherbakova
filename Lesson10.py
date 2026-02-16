# Задача 1
# Создай базовый класс Animal. У него должен быть метод __init__, который принимает имя животного (name) и сохраняет его в атрибут экземпляра.
# Также в классе Animal должен быть метод speak(), который ничего не делает (можно использовать pass).
#
# Затем создай два дочерних класса: Dog и Cat.
# Они должны наследовать от Animal и переопределять метод speak().
# В классе Dog метод speak() должен выводить на экран: "{name} says Woof!" (вместо {name} подставь имя собаки).
# В классе Cat метод speak() должен выводить на экран: "{name} says Meow!".

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")
dog = Dog(name="Собачка")
cat = Cat(name="Кошечка")
cat.speak()
dog.speak()

# Задача 2
# Создай базовый класс Vehicle (Транспортное средство).
# В __init__ он должен принимать два параметра: brand (марка) и model (модель), и сохранять их как атрибуты.
# Также добавь в базовый класс метод info(), который выводит на экран строку в формате: "Это транспортное средство: [brand] [model]".
#
# Затем создай дочерний класс Car (Автомобиль), который наследует от Vehicle.
# В классе Car переопредели метод info() так, чтобы он выводил: "Это автомобиль: [brand] [model]".
#
# Создай один экземпляр класса Car и вызови у него метод info().

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def info(self):
        print(f"Это транспортное средство: {self.brand} {self.model}")
class Car(Vehicle):
    def info(self):
        print(f"Это автомобиль: {self.brand} {self.model}")
car_1 =Car(brand="Ауди", model="A5")
car_1.info()

# Задача 3
#
# Создай базовый класс Employee (Сотрудник).
# В методе __init__ должны сохраняться атрибуты: name (имя) и salary (зарплата).
# Добавь метод get_info(), который возвращает (не печатает, а именно возвращает через return) строку вида: "Сотрудник: [name], Зарплата: [salary]".
#
# Затем создай дочерний класс Manager (Менеджер), который наследует от Employee.
# В классе Manager переопредели метод get_info() так, чтобы он возвращал строку: "Менеджер: [name], Зарплата: [salary]".
#
# Подсказка: Чтобы не дублировать код формирования строки полностью, внутри метода Manager.get_info() можно вызвать метод родителя и дополнить его.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def get_info(self):
        return f"Сотрудник: {self.name}, Зарплата: {self.salary}"
class Manager(Employee):
    def get_info(self):
        return f"Менеджер: {self.name}, Зарплата: {self.salary}"   # return super().get_info().replace("Сотрудник", "Менеджер")

# Задача 4
#
# Создай базовый класс Product (Товар).
# В __init__ сохрани атрибуты: name (название) и price (цена).
# Добавь метод get_price() который возвращает цену товара (просто число).
#
# Создай дочерний класс DiscountedProduct (Товар со скидкой), который наследует от Product.
# При создании товара со скидкой он должен принимать ещё один дополнительный параметр: discount (скидка в процентах, например 10 для 10%).
# В классе DiscountedProduct переопредели метод get_price() так, чтобы он возвращал цену с учётом скидки.
#
# Примечание:
# В __init__ дочернего класса нужно будет вызвать родительский __init__, чтобы сохранить name и price.
# В методе get_price дочернего класса нужно будет вызвать родительский get_price (через super()), чтобы получить исходную цену, а затем применить к ней скидку.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_price(self):
        return self.price
class DiscountedProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount
    def get_price(self):
        return super().get_price() * (100-self.discount)/100