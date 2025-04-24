#include <iostream>
#include <unordered_set>
#include <map>
using namespace std;

class Flight {
    public:
        Flight(string flight_number, string origin, string destination, int total_seats) {
            this->flight_number = flight_number;
            this->origin = origin;
            this->destination = destination;
            available_seats = this->total_seats = total_seats;
        }

        int getAvailableSeats() const { return available_seats; }
        string getFlightNumber() const {return flight_number; }

        bool book_seat(string passenger_name) {
            if (available_seats > 0) {
                passengers.insert(passenger_name);
                available_seats--;
                return true;
            } else {
                return false; 
            }
        }
        bool cancel_booking(string passenger_name) {
            if (passengers.find(passenger_name) != passengers.end()) {
                passengers.erase(passenger_name);
                available_seats++;
                return true;
            } else {
                return false;
            }
        }
    private:
        string flight_number, origin, destination;
        int total_seats, available_seats;
        unordered_set<string> passengers;
};
class BookingSystem {
    public:
        BookingSystem() = default;

        void add_flight(Flight flight) {
            flights.insert({ flight.getFlightNumber(), flight });
        }
        bool book_flight(string flight_number, string passenger_name) {
            return flights.at(flight_number).book_seat(passenger_name);
        }
        bool cancel_booking(string flight_number, string passenger_name) {
            return flights.at(flight_number).cancel_booking(passenger_name);
        }
    private:
        map<string, Flight> flights;
};

int main() {
    Flight flight1("BA123", "Seattle", "New York", 1);
    Flight flight2("BA456", "Seattle", "London", 150);

    BookingSystem booking_system;
    booking_system.add_flight(flight1);
    booking_system.add_flight(flight2);

    cout << boolalpha << booking_system.book_flight("BA123", "Alice") << endl;   // True
    cout << boolalpha << booking_system.book_flight("BA123", "Bob") << endl;     // False, no seats available
    cout << boolalpha << booking_system.cancel_booking("BA123", "Alice") << endl; // True
    cout << boolalpha << booking_system.book_flight("BA123", "Charlie") << endl; // True, seat freed up by Alice
    return 0;
}