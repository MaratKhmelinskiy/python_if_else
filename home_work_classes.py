#Задача с codewars с прошлого урока
class User: #какие может содержать обькты сам класс ?
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def output_cash(self, output_cash1):
        if output_cash1 <= self.balance:
            self.balance -= output_cash1

        else:
            print("Недостаточно средств на счете")


    def raschet(self):
        print(f'{self.name} {self.balance} {self.checking_account}')

Jeff = User('Jeff', 70, True)
print(Jeff)
Jeff.output_cash(10)
Jeff.raschet()


# Задание 1: Класс "Книга"
# Создайте класс Book, который будет представлять книгу. Класс должен содержать следующие атрибуты и методы:
#
# Атрибуты:
#
# title (название книги)
# author (автор книги)
# pages (количество страниц)
# current_page (текущая страница, на которой находится читатель, изначально равна 0)
# Методы:
#
# read_pages(num_pages): метод, который увеличивает значение current_page на указанное количество страниц.
# Если current_page превышает общее количество страниц, установите его в pages.
# book_info(): метод, который выводит информацию о книге в формате: \
# "Название: {title}, Автор: {author}, Страниц: {pages}, Текущая страница: {current_page}"

class Book:
    def __init__(self, title, author, pages = 10, current_page = 0):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = current_page

    def read_pages(self,num_pages):
        self.current_page + num_pages

    def book_info(self):
        print(f'Название: {self.title}, Автор : {self.author}, Страниц: {self.pages}, Текущая страница: {self.current_page}')



HP = Book('Harry Potter', 'Rowlling', 5, 2)
HP.read_pages(4)
HP.book_info()


# Задание 2: Класс "Банк"
# Создайте класс BankAccount, который будет представлять банковский счет.
# Класс должен содержать следующие атрибуты и методы:
#
# Атрибуты:
#
# account_number (номер счета)
# balance (баланс счета)
# Методы:
#
# deposit(amount): метод, который увеличивает баланс на указанную сумму.
# withdraw(amount): метод, который уменьшает баланс на указанную сумму.
# Если на счете недостаточно средств, выведите сообщение "Недостаточно средств".
# account_info(): метод, который выводит информацию о счете в формате:\
# "Счет №{account_number}, Баланс: {balance}"


#какие значения мы можем указаывать в атрибутах ?
class BankAccount: #как по другому отнять ?
    def __init__(self,account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):

        if self.balance <= 0:
            print('На счете недостаточно средств')
        else:
            self.balance -= amount

    def account_info(self):
        print(f' Счет № {self.account_number}, Баланс {self.balance}')

Rich = BankAccount('40817810', 100)

Rich.deposit(5)

Rich.account_info()

Rich.withdraw(50)

Rich.account_info()

Rich.withdraw(60)

Rich.account_info()

# Задание 3: Класс "Прямоугольник"
# Создайте класс Rectangle, который будет представлять прямоугольник. Класс должен содержать следующие атрибуты и методы:
#
# Атрибуты:
#
# width (ширина)
# height (высота)
# Методы:
#
# area(): метод, который возвращает площадь прямоугольника (ширина * высота).
# perimeter(): метод, который возвращает периметр прямоугольника (2 * (ширина + высота)).
# rectangle_info(): метод, который выводит информацию о прямоугольнике в формате: \
# "Ширина: {width}, Высота: {height}, Площадь: {area()}, Периметр: {perimeter()}"


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return  self.width * self.height #зачем return , если в предыдущем значении мне нужно было увеличить значение атрибута, а из-за retutn он не увеличивался

    def perimeter(self):
       return (self.width + self.height) * 2

    def rectangle_info(self):
        print(f'Ширина {self.width}, Высота {self.height}, Площадь {self.area()}, {self.perimeter()}')

data = Rectangle(5, 4)

data.area()
data.perimeter()

data.rectangle_info()