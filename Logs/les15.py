class Event:
    def __init__(self, title, date):
        self.title = title
        self.date = date

    def show(self):
        print(f"Подія: {self.title}")
        print(f"Дата: {self.date}")


class Meeting(Event):
    def __init__(self, title, date, place):
        super().__init__(title, date)  # виклик конструктора батьківського класу
        self.place = place

    # перевизначення методу
    def show(self):
        print(f"Зустріч: {self.title}")
        print(f"Дата: {self.date}")
        print(f"Місце: {self.place}")


# 🔹 Приклад використання
event = Event("Концерт", "10.02.2026")
event.show()

print("-----")

meeting = Meeting("Командна нарада", "12.02.2026", "Офіс 305")
meeting.show()

        


1#

class Notification:
    def __init__(self, message):
        self.message = message

    def send(self):
        print("Загальне сповіщення:", self.message)



2#

class EmailNotification(Notification):
    def send(self):
        print(f"📧 Email надіслано з текстом: {self.message}")


class SMSNotification(Notification):
    def send(self):
        print(f"📱 SMS надіслано з текстом: {self.message}")


class PushNotification(Notification):
    def send(self):
        print(f"🔔 Push-сповіщення: {self.message}")



3#

notifications = [
    EmailNotification("Вітаємо з реєстрацією!"),
    SMSNotification("Ваш код підтвердження: 1234"),
    PushNotification("У вас нове повідомлення")
]

for notification in notifications:
    notification.send()





1#


class Character:
    def __init__(self, name):
        self.name = name

    def attack(self):
        print(f"{self.name} атакує!")




2#


class Warrior(Character):
    def attack(self):
        print(f"{self.name} б'є мечем! ⚔️")


class Mage(Character):
    def attack(self):
        print(f"{self.name} кидає магічне закляття! ✨")


class Archer(Character):
    def attack(self):
        print(f"{self.name} стріляє з лука! 🏹")




3#


characters = [
    Warrior("Артур"),
    Mage("Мерлін"),
    Archer("Леголас")
]

for character in characters:
    character.attack()








1#


class Payment:
    def __init__(self, amount):
        self.amount = amount

    def pay(self):
        print(f"Оплата на суму {self.amount} грн")



2#

class CardPayment(Payment):
    def pay(self):
        print(f"💳 Оплата карткою на суму {self.amount} грн")


class CryptoPayment(Payment):
    def pay(self):
        print(f"🪙 Оплата криптовалютою на суму {self.amount} грн")


class CashPayment(Payment):
    def pay(self):
        print(f"💵 Оплата готівкою на суму {self.amount} грн")



3#

payments = [
    CardPayment(1500),
    CryptoPayment(0.025),
    CashPayment(500)
]

for payment in payments:
    payment.pay()
