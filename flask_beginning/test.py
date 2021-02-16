from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/", methods=["POST", "GET"])
def reset_data():
    if request.method == "POST":
        with open("login.txt", "w") as logins:
            logins.write("")
        return redirect(url_for("home", usr=user))


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        password = request.form["pswrd"]
        with open("login.txt", "a") as logins:
            logins.write(f"Login: {user} Password: {password} |\n")
        return redirect(url_for("home", usr=user))
    else:
        return render_template("login.html")


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
