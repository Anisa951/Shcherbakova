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


