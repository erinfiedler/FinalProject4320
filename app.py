from flask import Flask, render_template, request, redirect, url_for
import random, string
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
        adminFile = open('./passcodes.txt')
        for admin in adminFile.readlines():
            admin = admin.split(',')
            user = admin[0].strip()
            password = admin[1].strip()
            if request.form['username'] != user or request.form['password'] != password:
                continue
            else: 
                return render_template('admin.html')
        error = 'Invalid Credentials. Please try again.'
    else:
        return render_template('login.html', error=error)
    return render_template('login.html', error=error)

#admin page
@app.route("/admin")
def admin():
    total_sales = calculate_total_sales()
    chart_data = display_seating_chart()
    return render_template('admin.html', total_sales=total_sales, seating_chart=chart_data)

#reservation page
@app.route("/reservation")
def reservation():
    return render_template("make_reservation.html")

print("Welcome to the Trip Reservation System")

def generate_reservation_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

#pull up existing reservations
def load_reservations():
    reservations = []

    try:
        with open('reservations.txt', 'r') as file:
            for line in file:
                # Split each line into individual fields
                data = line.strip().split(', ')
                
                # Convert seat row and column to integers
                row, col = map(int, data[1:3])

                # Append the reservation data to the list
                reservations.append((data[0], row, col, data[3]))

    except FileNotFoundError:
        # Handle the case where the file is not found
        print("Error: reservations.txt not found.")
    except Exception as e:
        # Handle other potential errors
        print(f"Error loading reservations: {e}")

    return reservations

#save reservation data to file
def save_reservation(reservation):
        try:
            #res code
            reservation_code = generate_reservation_code()
            with open('reservations.txt', 'a') as file:
            # Convert seat row and column to strings for writing to file
                row, col = map(str, reservation[1:3])

            # Join reservation data into a string and write to file
                file.write(', '.join([reservation[0], row, col, reservation_code]) + '\n')\

        except Exception as e:
        # Handle errors while saving the reservation
            print(f"Error saving reservation: {e}")

#get cost matrix
def get_cost_matrix():
    cost_matrix = [[100, 75, 50, 100] for row in range(12)]
    return cost_matrix


# Inside your Flask route or function
@app.route('/seating_chart')
def seating_chart():
    # Generate or fetch seating chart data
    seating_chart_data = [['_' for _ in range(4)] for _ in range(12)]
    
    # Simulate some reserved seats
    seating_chart_data[0][0] = seating_chart_data[1][2] = 'X'

    return render_template('seating_chart.html', seating_chart_data=seating_chart_data)


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




if __name__ == '__main__':
    app.run(debug=True, port=5002)
