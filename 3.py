
#1

#try:
#    num = float(input("Введи число: "))
#    print("Ти ввів:", num)
#except ValueError:
#    print("Помилка: це не число")


#2

#try:
#    a = float(input("Введи перше число: "))
#    b = float(input("Введи друге число: "))
#    print("Результат:", a / b)
#except ValueError:
#    print("Помилка: потрібно вводити числа")
#except ZeroDivisionError:
#    print("Помилка: ділення на 0")


#3

#try:
#    age = int(input("Введи вік: "))
#    if age < 0:
#        print("Вік не може бути менше 0")
#    else:
#        print("Твій вік:", age)
#except ValueError:
 #   print("Помилка: вік має бути числом")


#4

#while True:
#    try:
#        num = float(input("Введи число: "))
#        print("Добре, це число:", num)
#        break
#    except ValueError:
#        print("Це не число, спробуй ще раз")


#5

#try:
#    a = float(input("Введи перше число: "))
#    b = float(input("Введи друге число: "))
#    op = input("Введи операцію (+ - * /): ")

#    if op == "+":
#        print(a + b)
#    elif op == "-":
#        print(a - b)
#    elif op == "*":
#        print(a * b)
#    elif op == "/":
#        try:
#            print(a / b)
#        except ZeroDivisionError:
#            print("Ділення на 0 неможливе")
#    else:
#        print("Невідома операція")
#except ValueError:
#    print("Помилка: введи числа")


#6

#arr = [10, 20, 30]

#try:
#    index = int(input("Введи індекс: "))
#    print("Елемент:", arr[index])
#except IndexError:
#    print("Помилка: індекс поза межами списку")
#except ValueError:
#    print("Помилка: індекс має бути числом")





# Перевірка пароля
#try:
#    password = input("Введи пароль: ")
#    if len(password) < 6:
#        raise ValueError("Пароль має містити мінімум 6 символів")
#    print("Пароль прийнято")
#except ValueError as e:
#    print("Помилка:", e)

# Перевірка числа від 1 до 10
#try:
#    num = int(input("Введи число від 1 до 10: "))
#    if num < 1 or num > 10:
#        raise ValueError("Число поза діапазоном 1–10")
#    print("Число правильне:", num)
#except ValueError as e:
#    print("Помилка:", e)




#while True:
#    try:
#        num = float(input("Введи число: "))
#        result = 100 / num
#        print("100 /", num, "=", result)
#        break
#    except ValueError:
#        print("Помилка: потрібно ввести число")
#    except ZeroDivisionError:
#        print("Помилка: на 0 ділити не можна")




attempts = 3

while attempts > 0:
    try:
        num = float(input("Введи число: "))
        print("Число прийнято:", num)
        break
    except ValueError:
        attempts -= 1
        print("Помилка: це не число")
        print("Залишилось спроб:", attempts)

if attempts == 0:
    print("Помилка: спроби закінчились")



try:
    password = input("Введи пароль: ")

    if len(password) < 8:
        raise ValueError("Пароль має містити щонайменше 8 символів")

    if not any(char.isdigit() for char in password):
        raise ValueError("Пароль має містити хоча б одну цифру")

    if not any(char.isalpha() for char in password):
        raise ValueError("Пароль має містити хоча б одну літеру")

    print("Пароль прийнято")

except ValueError as e:
    print("Помилка:", e)
