from Main_Flight.Operations import flight_Details as f
from Main_Flight.Operations import Ticket_Booking as t
from Main_Flight.Operations import Booking_Cancel as b
from Main_Flight.Operations import Display_Ticket as d
from Main_Flight.Operations import Ticket_Update as u

while True:
    print('''
    WELCOME TO THE AIRLINE RESERVATION SYSTEM
    1. Fetch the Flight Schedule
    2. Reservation
    3. Update Ticket Info
    4. Cancel Ticket
    5. Display Ticket
    6. Exit from App
    ''')
    print("choose any option from the above")
    ch = int(input())
    if ch == 1:
        f.get_flightDetails()
        print("------------------------------------------------------------------")
    elif ch == 2:
        t.book_ticket()
        print("------------------------------------------------------------------")
    elif ch == 3:
        u.update_info()
        print("------------------------------------------------------------------")
    elif ch == 4:
        b.cancel_ticket()
        print("------------------------------------------------------------------")
    elif ch == 5:
        d.display_ticket()
        print("------------------------------------------------------------------")
    else:
        break