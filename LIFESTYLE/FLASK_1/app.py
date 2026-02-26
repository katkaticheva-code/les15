from flask import Flask, abort

app = Flask(__name__)

@app.route("/")
def home():
    return "Вітаю! Це простий сервер на Flask."

@app.route("/about")
def about():
    return "Автор: Твоє ім'я. Початківець Python-розробник 🚀"

@app.route("/skills")
def skills():
    return "Мої навички: Python, Flask, HTML, CSS"

@app.route("/contact")
def contact():
    return "Контакти: email@example.com | Telegram: @username"

# 2️⃣ Температура
@app.route("/temperature/<int:t>")
def temperature(t):
    if t < 0:
        return "Мороз ❄️"
    elif 0 <= t < 20:
        return "Прохолодно 🌬️"
    elif 20 <= t < 30:
        return "Тепло 🌤️"
    else:
        return "Спека 🔥"

# 3️⃣ Міні-калькулятор
@app.route("/math/<operation>/<int:a>/<int:b>")
def math(operation, a, b):
    if operation == "add":
        return str(a + b)
    elif operation == "sub":
        return str(a - b)
    elif operation == "mul":
        return str(a * b)
    elif operation == "div":
        if b == 0:
            return "Помилка: ділення на нуль 😅"
        return str(a / b)
    else:
        abort(404)

if __name__ == "__main__":
    app.run(debug=True)