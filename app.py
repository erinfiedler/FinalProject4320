from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

print("Welcome to the Trip Reservation System")

if __name__ == '__main__':
    app.run(debug=True)
