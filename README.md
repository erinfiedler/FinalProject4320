# Scrum Team 8 FinalProject4320

The bus can seat up to 48 people, 12 rows of 4 seats each
A. Create a seating chart and load the initial reservations
B. Display the main menu that asks the user whether they want to reserve a seat or log in as an administrator
C. If the user selects the admin login option they are taken to a page with a form to login. Information the user provides:
admin username
admin password
D. If the user successfully logs in a seating chart is displayed along with the total sales collected.
E. If the user selects the the reservation option they are taken to a page with a form to reserve a seat. Information the user provides
first name
last name
seat row
seat column
F. Display a flight chart
G. Calculate and get the total sales for the flight when the user successfully logs in as an admin
H. Create and print a reservation code for the user when the user successfully makes a reservation
I. Save the reservation in formation the reservation.txt (first name, seat row, seat column, e_ticket number)
J. Each page should have a link to the main option page.

Cost Matrix: You will need pricing a matrix to calculate sales for the flight. The following python function will create a 12 x 4 cost matrix which represents the cost of each seat on the flight. You should use this code in your project.

'''
Function to generate cost matrix for flights
Input: none
Output: Returns a 12 x 4 matrix of prices
'''
def get_cost_matrix():
    cost_matrix = [[100, 75, 50, 100] for row in range(12)]
    return cost_matrix

 
