from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

database = []


@app.route("/")
def index():
    return render_template("index.html", database=database)

@app.route("/add", methods=["POST"])
def add():
    name = request.form['name']
    database.append({"task": name, "done": False})
    return redirect(url_for("index"))


@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    if request.method == "POST":
        database[index]["task"] = request.form['name']
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", database=database, index=index)


@app.route("/delete/<int:index>")
def delete(index):
    del database[index]
    return redirect(url_for("index"))


@app.route("/check/<int:index>", methods=["POST"])
def check(index):
    data = database[index]
    data["done"] = not data["done"]
    return redirect(url_for("index"))
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)