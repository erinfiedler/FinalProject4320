from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return render_template('admin.html')
    return render_template('login.html', error=error)

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/reservation")
def reservation():
    return render_template("make_reservation.html")

print("Welcome to the Trip Reservation System")

#get cost matrix
def get_cost_matrix():
    cost_matrix = [[100, 75, 50, 100] for row in range(12)]
    return cost_matrix

if __name__ == '__main__':
    app.run(debug=True)
