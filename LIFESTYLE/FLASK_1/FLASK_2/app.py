#from flask import Flask, request, render_template_string

#app = Flask(__name__)

#@app.route('/form', methods=['GET', 'POST'])
#def form():
#    if request.method == "POST":
#        name = request.form.get('name')
#        return render_template_string(f"<h1>Hello {name}!</h1>")
#    return '''
#    <form method="post">
#        <input type="text" name="name" placeholder="Enter your name">
#        <input type="submit" value="Submit">
#    </form>
#    '''

#if __name__ == "__main__":
#    app.run(debug=True)


from flask import Flask, request, render_template

app = Flask(__name__)

tasks = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)
    return render_template("index.html", tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)



