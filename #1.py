
import json
import os

FILE_NAME = "planner.json"


def load_events():
    """
    1. Спробувати відкрити файл planner.json
    2. Якщо файлу немає — повернути порожній словник і event_id = 1
    3. Якщо файл є — завантажити дані
    4. Повернути planner та наступний event_id
    """
    if not os.path.exists(FILE_NAME):
        return {}, 1

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        planner = json.load(file)

    if planner:
        event_id = max(map(int, planner.keys())) + 1
    else:
        event_id = 1

    return planner, event_id


def save_events(planner):
    """
    1. Зберегти planner у файл planner.json
    """
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(planner, file, ensure_ascii=False, indent=4)


def show_menu():
    print("\n--- Персональний планувальник ---")
    print("1. Додати подію")
    print("2. Переглянути всі події")
    print("3. Видалити подію")
    print("4. Знайти події за датою")
    print("5. Вийти")


def add_event(planner, event_id):
    """
    1. Запитати назву, дату, час, опис
    2. Створити подію
    3. Додати її в planner
    4. Зберегти файл
    5. Повернути новий event_id
    """
    title = input("Назва події: ")
    date = input("Дата (YYYY-MM-DD): ")
    time = input("Час (HH:MM): ")
    description = input("Опис: ")

    planner[str(event_id)] = {
        "title": title,
        "date": date,
        "time": time,
        "description": description
    }

    save_events(planner)
    print("Подію додано!")

    return event_id + 1


def show_events(planner):
    """
    1. Якщо подій немає — вивести повідомлення
    2. Вивести всі події у зручному форматі
    """
    if not planner:
        print("Подій поки немає.")
        return

    for event_id, event in planner.items():
        print(f"""
ID: {event_id}
Назва: {event['title']}
Дата: {event['date']}
Час: {event['time']}
Опис: {event['description']}
-------------------------
""")


def delete_event(planner):
    """
    1. Запитати ID події
    2. Видалити подію зі словника
    3. Зберегти файл
    """
    event_id = input("Введіть ID події для видалення: ")

    if event_id in planner:
        del planner[event_id]
        save_events(planner)
        print("Подію видалено.")
    else:
        print("Подію з таким ID не знайдено.")


def find_by_date(planner):
    """
    1. Запитати дату
    2. Знайти та вивести події
    """
    date = input("Введіть дату (YYYY-MM-DD): ")
    found = False

    for event_id, event in planner.items():
        if event["date"] == date:
            print(f"""
ID: {event_id}
Назва: {event['title']}
Час: {event['time']}
Опис: {event['description']}
-------------------------
""")
            found = True

    if not found:
        print("Подій на цю дату не знайдено.")


def main():
    planner, event_id = load_events()

    while True:
        show_menu()
        choice = input("Оберіть дію: ")

        if choice == "1":
            event_id = add_event(planner, event_id)
        elif choice == "2":
            show_events(planner)
        elif choice == "3":
            delete_event(planner)
        elif choice == "4":
            find_by_date(planner)
        elif choice == "5":
            print("До побачення!")
            break
        else:
            print("Невірний вибір")


if __name__ == "__main__":
    main()


