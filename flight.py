class Flight:
    def __init__(self, number, source, destination, departure, arrival, price, seats):
        self.number = number
        self.source = source
        self.destination = destination
        self.departure = departure
        self.arrival = arrival
        self.price = price
        self.seats = seats

    def __str__(self):  # Corrected method name
        return (f"Flight {self.number}: {self.source} → {self.destination}, "
                f"Departure: {self.departure}, Arrival: {self.arrival}, "
                f"Price: ₹{self.price}, Seats: {self.seats}")


class FlightReservationSystem:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def display_flights(self):
        if not self.flights:
            print("No flights available.")
        else:
            for f in self.flights:
                print(f)

    def search_by_number(self, number):
        for f in self.flights:
            if f.number == number:
                return f
        return None

    def search_by_destination(self, destination):
        result = [f for f in self.flights if f.destination.lower() == destination.lower()]
        return result

    def book_ticket(self, number):
        f = self.search_by_number(number)
        if f:
            if f.seats > 0:
                f.seats -= 1
                print(f"✅ Ticket booked on Flight {f.number}. Remaining seats: {f.seats}")
            else:
                print("❌ No seats available!")
        else:
            print("❌ Flight not found!")

    def cancel_ticket(self, number):
        f = self.search_by_number(number)
        if f:
            f.seats += 1
            print(f"✅ Ticket cancelled on Flight {f.number}. Seats now: {f.seats}")
        else:
            print("❌ Flight not found!")

    def sort_by_price(self):
        self.flights.sort(key=lambda x: x.price)
        print("📊 Flights sorted by price.")

    def sort_by_departure(self):
        self.flights.sort(key=lambda x: x.departure)
        print("📅 Flights sorted by departure time.")


# ---------------- Main Program ----------------
if __name__ == "__main__":
    system = FlightReservationSystem()

    # Sample flights
    system.add_flight(Flight("AI101", "Mumbai", "Delhi", "08:00", "10:00", 4500, 3))
    system.add_flight(Flight("AI102", "Pune", "Bangalore", "09:30", "11:30", 4000, 2))
    system.add_flight(Flight("AI103", "Delhi", "Chennai", "06:45", "09:15", 5000, 5))

    while True:
        print("\n===== ✈️ Flight Reservation System =====")
        print("1. Display All Flights")
        print("2. Add Flight")
        print("3. Search Flight by Number")
        print("4. Search Flights by Destination")
        print("5. Book Ticket")
        print("6. Cancel Ticket")
        print("7. Sort Flights by Price")
        print("8. Sort Flights by Departure Time")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            system.display_flights()

        elif choice == "2":
            num = input("Enter Flight Number: ")
            src = input("Enter Source: ")
            dest = input("Enter Destination: ")
            dep = input("Enter Departure Time (HH:MM): ")
            arr = input("Enter Arrival Time (HH:MM): ")
            price = int(input("Enter Price: "))
            seats = int(input("Enter Available Seats: "))
            system.add_flight(Flight(num, src, dest, dep, arr, price, seats))
            print("✅ Flight added successfully!")

        elif choice == "3":
            num = input("Enter Flight Number to Search: ")
            f = system.search_by_number(num)
            print(f if f else "❌ Flight not found!")

        elif choice == "4":
            dest = input("Enter Destination to Search: ")
            result = system.search_by_destination(dest)
            if result:
                for f in result:
                    print(f)
            else:
                print("❌ No flights found for that destination.")

        elif choice == "5":
            num = input("Enter Flight Number to Book: ")
            system.book_ticket(num)

        elif choice == "6":
            num = input("Enter Flight Number to Cancel: ")
            system.cancel_ticket(num)

        elif choice == "7":
            system.sort_by_price()
            system.display_flights()

        elif choice == "8":
            system.sort_by_departure()
            system.display_flights()

        elif choice == "9":
            print("👋 Exiting... Thank you!")
            break

        else:
            print("❌ Invalid choice! Try again.")
