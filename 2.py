

#1

from datetime import datetime

text = input("Запис у щоденник: ")

with open("diary.txt", "a", encoding="utf-8") as f:
    f.write(f"{datetime.now()}: {text}\n")

print("Запис збережено")


#2

with open("grades.txt", "r") as f:
    grades = list(map(int, f.read().split()))

average = sum(grades) / len(grades)
print("Середнє:", average)


#3

login = input("Логін: ")
password = input("Пароль: ")

with open("users.txt", "a") as f:
    f.write(f"{login}:{password}\n")

print("Користувач збережений")


#4

import os

filename = "data.txt"

if os.path.exists(filename):
    with open(filename) as f:
        print(f.read())
else:
    print("Файл не існує")


#5

a = float(input("a: "))
b = float(input("b: "))
result = a + b

with open("calc_history.txt", "a") as f:
    f.write(f"{a} + {b} = {result}\n")

print("Результат:", result)


#6

import json

event = {
    "title": input("Подія: "),
    "date": input("Дата: "),
    "time": input("Час: ")
}

with open("events.json", "a", encoding="utf-8") as f:
    json.dump(event, f, ensure_ascii=False)
    f.write("\n")

print("Подію збережено")


#7

with open("numbers.txt") as f:
    numbers = list(map(int, f.read().split()))

numbers.sort()

with open("sorted_numbers.txt", "w") as f:
    f.write(" ".join(map(str, numbers)))

print("Дані відсортовано")

