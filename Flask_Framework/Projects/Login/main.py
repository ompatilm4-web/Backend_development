from flask import Flask, render_template, request, redirect, url_for
import data

app = Flask(__name__)


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        user_email = request.form.get("email")
        user_password = request.form.get("password")
        user_Data = data.fetch_Data()

        for db_name, db_email, db_password in user_Data:
            if (user_email == db_email and user_password == db_password):
                message = f"Login Successful {db_name}"
                return render_template("welcome.html",message=message)
        return render_template("login.html",error="Invalid Credentials")
    return render_template("login.html")



@app.route("/welcome")
def welcome():
    return render_template("welcome.html",message="Welcome User")



@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        data.InsertData(name,email,password)
        return redirect("/login")

    return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug=True)