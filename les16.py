1#

class User:
    def __init__(self, balance=0):
        self.balance = balance  # йде через сеттер

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Баланс не може бути від’ємним")
        self.__balance = value



2#

class Person:
    def __init__(self, age):
        self.age = age  # через сеттер

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Вік має бути цілим числом")
        if not (0 <= value <= 120):
            raise ValueError("Вік має бути в діапазоні від 0 до 120")
        self.__age = value


3#

class Thermometer:
    def __init__(self, temperature=0):
        self.temperature = temperature  # через сеттер

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if not (-50 <= value <= 50):
            raise ValueError("Температура має бути в межах від -50 до +50")
        self.__temperature = value


4#

class Product:
    def __init__(self, price):
        self.price = price  # через сеттер

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Ціна не може бути від’ємною")
        self.__price = value


5#

class Car:
    def __init__(self, speed=0):
        self.speed = speed  # через сеттер

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > 200:
            raise ValueError("Швидкість не може перевищувати 200 км/год")
        if value < 0:
            raise ValueError("Швидкість не може бути від’ємною")
        self.__speed = value


6#

class UserAccount:
    def __init__(self, password):
        self.password = password  # через сеттер

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if len(value) < 6:
            raise ValueError("Пароль має містити щонайменше 6 символів")
        self.__password = value





