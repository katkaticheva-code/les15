from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Мій міні-додаток</h1>
    <ul>
        <li><a href="/profile">1. Мій профіль</a></li>
        <li><a href="/temperature/25">2. Створити маршрут</a></li>
        <li><a href="/calculator">3. Міні-калькулятор</a></li>
    </ul>
    """

@app.route("/profile")
def profile():
    return """
    <h2>Мій профіль</h2>
    <p>Автор: Катя</p>
    <p>Навички: Python, Flask, HTML, CSS</p>
    <p>Контакти: email@example.com</p>
    <a href="/">Назад</a>
    """

@app.route("/temperature/<int:t>")
def temperature(t):
    if t < 0:
        result = "Мороз ❄️"
    elif 0 <= t < 20:
        result = "Прохолодно 🧥"
    elif 20 <= t < 30:
        result = "Тепло 😎"
    else:
        result = "Спека 🔥"

    return f"""
    <h2>Температура: {t}°C</h2>
    <p>{result}</p>
    <a href="/">Назад</a>
    """

@app.route("/calculator")
def calculator():
    return """
    <h2>Міні-калькулятор</h2>

    <form action="/calc" method="get">
        <label>Перше число (a):</label><br>
        <input type="number" name="a" required><br><br>

        <label>Операція:</label><br>
        <select name="op">
            <option value="add">add (+)</option>
            <option value="sub">sub (-)</option>
            <option value="mul">mul (*)</option>
            <option value="div">div (/)</option>
        </select><br><br>

        <label>Друге число (b):</label><br>
        <input type="number" name="b" required><br><br>

        <button type="submit">Обчислити</button>
    </form>

    <br>
    <a href="/">Назад</a>
    """

@app.route("/calc")
def calc():
    try:
        a = float(request.args.get("a", ""))
        b = float(request.args.get("b", ""))
        op = request.args.get("op", "")
    except ValueError:
        return """
        <h2>Помилка</h2>
        <p>Введіть правильні числа.</p>
        <a href="/calculator">Назад</a>
        """

    if op == "add":
        result = a + b
        sign = "+"
    elif op == "sub":
        result = a - b
        sign = "-"
    elif op == "mul":
        result = a * b
        sign = "*"
    elif op == "div":
        if b == 0:
            return """
            <h2>Помилка 😅</h2>
            <p>Ділення на нуль!</p>
            <a href="/calculator">Назад</a>
            """
        result = a / b
        sign = "/"
    else:
        abort(404)

    return f"""
    <h2>Результат</h2>
    <p>{a} {sign} {b} = <b>{result}</b></p>
    <a href="/calculator">Назад</a>
    """

if __name__ == "__main__":
    app.run(debug=True)