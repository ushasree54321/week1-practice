seats = [
    "Available",
    "Booked",
    "Available",
    "Available",
    "Booked",
    "Available",
    "Booked",
    "Available"
]

print("Bus Seat Status:")

for i in range(len(seats)):
    print("Seat", i + 1, ":", seats[i])

seat_number = int(input("\nEnter seat number to book: "))

if seats[seat_number - 1] == "Available":
    seats[seat_number - 1] = "Booked"
    print("Seat booked successfully.")
else:
    print("Seat is already booked.")

booked_seats = 0
available_seats = 0

for seat in seats:
    if seat == "Booked":
        booked_seats += 1
    else:
        available_seats += 1

print("\nTotal Seats:", len(seats))
print("Booked Seats:", booked_seats)
print("Available Seats:", available_seats)