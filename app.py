from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#return to main menu
@app.route("/")
def home():
    return render_template("index.html")

#admin authentication
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return render_template('admin.html')
    return render_template('login.html', error=error)

#admin page
@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/reservation")
def reservation():
    return render_template("make_reservation.html")

print("Welcome to the Trip Reservation System")

#save reservation data to file
def save_reservation(reservation):
    #save reservations to text file
    pass

#display seating chart
def seating_chart():
    pass

#reserve seat
@app.route('/reserve', methods=['GET', 'POST'])
def reserve_seat():
    if request.method == 'POST':
        # Process reservation form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        seat_row = int(request.form['seat_row'])
        seat_column = int(request.form['seat_column'])

        # Implement seat reservation logic
        # Check if the seat is available, calculate price, generate e_ticket number, etc.

        # Save reservation
        reservation = (first_name, seat_row, seat_column, 'e_ticket_number')
        save_reservation(reservation)

        # Display reservation code
        return render_template('reservation_success.html', reservation_code='e_ticket_number')

    return render_template('reserve_seat.html', cost_matrix=get_cost_matrix())
#get cost matrix
def get_cost_matrix():
    cost_matrix = [[100, 75, 50, 100] for row in range(12)]
    return cost_matrix


if __name__ == '__main__':
    app.run(debug=True)
