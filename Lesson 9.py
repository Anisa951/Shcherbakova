# Задача 1
# Создай класс Book. У класса должен быть общий атрибут material = "бумага".
# Создай два экземпляра этого класса (две книги) и выведи на экран, из какого материала сделаны обе книги.

class Book:
    material = "бумага"

book_1 = Book()
book_2 = Book()

print(f" Первая книга из материала: {book_1.material}")
print (f" Вторая книга из материала: {book_2.material}")

#Задача 2
# Создай класс Car. У каждой машины должны быть индивидуальные атрибуты: color и speed (максимальная скорость).
# Создай две машины с разными цветами и скоростями. Выведи информацию о каждой машине в формате:
# "Автомобиль [цвет] едет со скоростью [скорость] км/ч"

class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def info(self):
        print(f"Автомобиль {self.color} едет со скоростью {self.speed} км/ч")

car_1 = Car(color="Красный", speed=120)
car_2 = Car(color="Синий", speed=100)
car_1.info()
car_2.info()

# Задача 3
# Создай класс Employee (сотрудник).
# У каждого сотрудника должны быть:
# индивидуальные атрибуты: name (имя) и position (должность)
# общий атрибут company = "Рога и Копыта"
# Создай двух сотрудников с разными именами и должностями.
# Выведи информацию о каждом сотруднике в формате:
# "Имя: [имя], должность: [должность], компания: [название компании]"

class Employee:
    company = "Рога и Копыта"


    def __init__(self, name, position):
        self.name = name
        self.position = position

    def info(self):
        print(f"Имя: {self.name}, должность: {self.position}, компания: {self.company}")

human_1 = Employee(name="Александр", position="Менеджер")
human_2 = Employee(name="Евгения", position="Руководитель отдела")
human_1.info()
human_2.info()

# Задача 4
# Создай класс Student.
# У студента должны быть:
# индивидуальные атрибуты: name (имя) и grade (оценка, число от 1 до 5)
# общий атрибут school = "Школа программирования"
# Создай трёх студентов с разными именами и оценками.
# Напиши метод is_excellent(), который будет возвращать True, если оценка студента 5, и False в противном случае.
# Выведи информацию о каждом студенте и результате метода is_excellent().

class Student:
    school = "Школа программирования"

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def is_excellent(self):
        if self.grade == 5:
            return True
        else:
            return False

    def info(self):
        print(f"Студент:{self.name}, Оценка: {self.grade}")

student_1 = Student(name="Александр", grade=2)
student_2 = Student(name="Евгений", grade=5)
student_3 = Student(name="Владимир", grade=4)
student_1.info()
student_2.info()
student_3.info()

print(student_1.is_excellent())
print(student_2.is_excellent())
print(student_3.is_excellent())

# Задача 5
# Создай класс Rectangle (прямоугольник).
# У прямоугольника должны быть индивидуальные атрибуты: width (ширина) и height (высота).
# Реализуй метод area(), который возвращает площадь прямоугольника.
# Создай два прямоугольника с разными размерами.
# Для каждого выведи сообщение:
# "Прямоугольник [ширина]x[высота] имеет площадь [площадь]"

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def info(self):
        print(f"Прямоугольник {self.width}х{self.height} имеет площадь {self.area()}")

s_1 = Rectangle(width=10, height=2)
s_2 = Rectangle(width=15, height=30)
s_1.info()
s_2.info()

# Задача 6
# Создай класс Counter (счётчик).
# У счётчика должен быть:
# индивидуальный атрибут value (начальное значение, по умолчанию 0)
# общий атрибут total_counters = 0 (сколько всего экземпляров класса было создано)
# При создании каждого нового счётчика общий атрибут total_counters должен увеличиваться на 1.
# Реализуй метод increment(), который увеличивает значение конкретного счётчика на 1.
# Создай два счётчика.
# Для каждого:
# вызови increment() несколько раз
# выведи его текущее значение
# В конце выведи общее количество созданных счётчиков.

class Counter:
    total_counters = 0

    def __init__(self, value=0):
        self.value = value
        Counter.total_counters += 1
    def increment(self):
        self.value += 1
c_1 = Counter(value=1)
c_2 = Counter(value=2)
c_1.increment()
c_1.increment()
c_2.increment()
c_2.increment()
print(c_1.value)
print(c_2.value)
print(Counter.total_counters)

# Задача 7
# Создай класс Dog.
# У собаки должны быть:
# индивидуальные атрибуты: name (кличка) и age (возраст)
# общий атрибут species = "собака"
# Реализуй метод bark(), который возвращает строку "Гав!".
# Реализуй метод human_age(), который возвращает возраст собаки в «человеческих» годах (собачий возраст × 7).
# Создай двух собак с разными кличками и возрастами.
# Для каждой:
# выведи строку:
# "[Кличка] — [вид]. Возраст: [возраст] лет, в человеческих годах: [возраст×7]"
# вызови метод bark() и напечатай результат.

class Dog:
    species = "собака"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        return "Гав!"
    def human_age(self):
        return self.age*7
    def info(self):
        print(f"{self.name} — {self.species}. Возраст: {self.age} лет, в человеческих годах: {self.human_age()}")
dog_1 = Dog(name="Жучка", age=20)
dog_2 = Dog(name="Рекс", age=10)
dog_1.info()
dog_2.info()
print(dog_1.bark())
print(dog_2.bark())

# Задача 8
# Создай класс BankAccount (банковский счёт).
# У счёта должны быть:
# индивидуальные атрибуты: owner (владелец) и balance (баланс, по умолчанию 0)
# общий атрибут bank_name = "Просто Банк"
# Реализуй методы:
# deposit(amount) — пополнение счёта (увеличивает баланс). Ничего не возвращает, только меняет баланс.
# withdraw(amount) — снятие денег.
# Если на счёте достаточно средств, уменьшает баланс и возвращает True.
# Если недостаточно, возвращает False и не меняет баланс.
# info() — выводит информацию:
# "Владелец: [имя], Баланс: [сумма], Банк: [название банка]"
# Создай два счёта с разными владельцами и начальными балансами (можно с 0, можно с любой суммой).
# Выполни несколько операций:
# Пополни первый счёт на 500.
# Сними со второго счёта сумму, которая доступна (чтобы вернулось True).
# Сними со второго счёта сумму, которая недоступна (чтобы вернулось False).
# Выведи info() по каждому счёту после операций.
# Также выведи результаты (True/False) операций снятия.

class BankAccount:
    bank_name = "Просто Банк"
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):    #пополнение счета
        self.balance += amount
    def withdraw(self, amount):          #снятие денег
        if self.balance >= amount:
            self.balance -= amount
            return True
        else :
            return False
    def info(self):
        print(f"Владелец: {self.owner}, Баланс: {self.balance}, Банк: {self.bank_name}")
c_1 = BankAccount(owner = "Владелец1", balance = 1000)
c_2 = BankAccount(owner="Владелец2", balance=100)
c_1.deposit(500)
c_2.withdraw(50)
c_2.withdraw(200)
c_1.info()
c_2.info()

# Задача 9
# Создай класс Smartphone.
# У смартфона должны быть:
# индивидуальные атрибуты: brand (бренд), model (модель), battery_level (уровень заряда, от 0 до 100, по умолчанию 100)
# общий атрибут power_on = True (включён ли телефон — по умолчанию все телефоны включены)
# Реализуй методы:

# charge(amount) — увеличивает заряд на amount, но не выше 100. Ничего не возвращает.

# use(amount) — уменьшает заряд на amount, но не ниже 0. Ничего не возвращает.

# info() — выводит информацию:

# "[Бренд] [Модель], заряд: [уровень]%, статус: [Включён/Выключен]"
# Статус зависит от power_on: если True — "Включён", если False — "Выключен".
# Создай два смартфона с разными брендами и моделями, с разным начальным зарядом (можно не 100).
# Выполни действия:
# Первый: заряди на 30, затем используй на 50.
# Второй: используй на 120 (должен упасть до 0, но не ниже).
# Выведи info() для каждого после операций.

class Smartphone:
    power_on = True
    def __init__(self, brand, model, battery_level=100):
        self.brand = brand
        self.model = model
        self.battery_level = battery_level
    def charge(self, amount):
        self.battery_level = min(self.battery_level + amount, 100)
    def use(self, amount):
        self.battery_level = max(self.battery_level - amount, 0)
    def info(self):
        print(f"{self.brand} {self.model}, заряд: {self.battery_level}%, статус: {'Включён' if self.power_on else 'Выключен'}")
phone_1 = Smartphone(brand="Nokia", model = 3300, battery_level=100)
phone_2 = Smartphone(brand="Apple", model = 17, battery_level=20)
phone_1.charge(30)
phone_1.use(50)
phone_2.use(120)
phone_1.info()
phone_2.info()

# Задача 10
# Создай класс Note (заметка).
# У заметки должны быть:
# индивидуальные атрибуты: title (заголовок) и content (содержание)
# общий атрибут notes_count = 0 (сколько всего заметок создано)
# При создании каждой новой заметки общий атрибут notes_count должен увеличиваться на 1.
# Реализуй методы:
# edit(new_content) — заменяет содержание заметки на новое. Ничего не возвращает.
# display() — выводит информацию в формате:
# "Заголовок: [title]\nСодержание: [content]"
# total_notes() — метод класса (используй @classmethod), который возвращает общее количество заметок.
# Создай три заметки с разными заголовками и содержанием.
# Выполни действия:
# Выведи каждую заметку через display().
# Измени содержание второй заметки.
# Выведи вторую заметку повторно, чтобы увидеть изменения.
# Выведи общее количество заметок, используя метод total_notes().

class Note:
    notes_count = 0
    def __init__(self, title, content):
        self.title = title
        self.content = content
        Note.notes_count += 1
    def edit(self, new_content):
        self.content = new_content
    def display(self):
        print (f"Заголовок: {self.title}\nСодержание: {self.content}")
    @classmethod
    def total_notes(cls):
        return cls.notes_count
note_1 = Note(title="Заголовок1", content="Содержание1")
note_2 = Note(title="Заголовок2", content="Содержание2")
note_3 = Note(title="Заголовок3", content="Содержание3")
note_1.display()
note_2.display()
note_3.display()
note_2.edit(new_content="Что-то новое")
note_2.display()
print(Note.total_notes())

# Задача 11
# Создай класс Product (товар).
# У товара должны быть:
# индивидуальные атрибуты: name (название), price (цена), quantity (количество на складе, по умолчанию 0)
# общий атрибут tax_rate = 0.2 (ставка налога, 20%)
# Реализуй методы:
# add_stock(amount) — увеличивает количество на складе на amount.
# sell(amount) — уменьшает количество на складе на amount.
# Если на складе достаточно товара (quantity >= amount) — уменьшает и возвращает True.
# Если недостаточно — возвращает False, количество не меняется.
# total_price() — возвращает общую стоимость всех товаров на складе с учётом налога:
# (price * quantity) * (1 + tax_rate)
# Создай два товара с разными названиями, ценами и начальным количеством.
# Выполни действия:
# Добавь складской запас первому товару.
# Продай со второго товара доступное количество (вернётся True).
# Продай со второго товара недоступное количество (вернётся False).
# Выведи общую стоимость с учётом налога для каждого товара.
# Все результаты операций (True/False от продаж, общую стоимость) — напечатай

class Product:
    tax_rate = 0.2
    def __init__(self, name, price, quantity=0 ):
        self.name = name
        self.price = price
        self.quantity = quantity
    def add_stock(self, amount):
        self.quantity += amount
    def sell(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
            return True
        else:
            return False
    def total_price(self):
        return (self.price * self.quantity) * (1 + self.tax_rate)
tovar_1 = Product(name="Товар1", price=100, quantity=10)
tovar_2 = Product(name="Товар2", price=500, quantity=2)
tovar_1.add_stock(10)
tovar_2.add_stock(10)
print(tovar_2.sell(20))
print(tovar_2.sell(2000))
print(tovar_1.total_price())
print(tovar_2.total_price())

# Задача 12
# Создай класс Cat.
# У кота должны быть:
# индивидуальные атрибуты: name (кличка) и age (возраст)
# общий атрибут species = "кошка"
# Реализуй метод meow(), который возвращает строку "Мяу!".
# Создай двух котов с разными именами и возрастами.
# Выведи информацию о каждом коте в формате:
# "[Имя], [возраст] лет, [вид]"
# И вызови метод meow() для каждого кота, напечатав результат.

class Cat:
    species = "кошка"
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def meow(self):
        return "Мяу!"
    def info(self):
        print(f"{self.name}, {self.age} лет, {self.species}")
cat_1 = Cat(name="Фродо", age=10)
cat_2 = Cat(name="Дымка", age=20)

print(cat_1.meow())
print(cat_2.meow())
cat_1.info()
cat_2.info()

# Задача 13
# Создай класс Book (книга).
# У книги должны быть:
# индивидуальные атрибуты: title (название), author (автор), year (год издания)
# общий атрибут genre = "художественная литература"
# Реализуй метод get_age(), который возвращает возраст книги (текущий год — год издания).
# Текущий год просто укажи 2025 прямо в коде (не нужно импортировать модули).
# Создай две книги с разными названиями, авторами и годами издания.
# Выведи информацию о каждой книге в формате:
# "[Название]", автор [автор], [год] г. (возраст: [возраст] лет), жанр: [жанр]"

class Book:

    genre = "художественная литература"

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_age(self):
        return 2025-self.year

    def info(self):
        print(f"{self.title}, автор {self.author}, {self.year} г. (возраст: {self.get_age()}, жанр: {self.genre})")

book_1 = Book(title= "Атака титанов1", author= "Исаяма", year= 2013)
book_2 = Book(title= "Наруто", author= "Кишимото", year= 1998)
book_1.info()
book_2.info()
