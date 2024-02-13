"""
Summary:
    Model for aircraft flights.

Usage:
    # Create an Aircraft object
    aircraft_instance = Aircraft(registration="ABC123", model="Boeing 737", num_rows=20, num_seats_per_row=6)

    # Create a Flight object, passing the Aircraft object as an argument
    flight_instance = Flight(number="AB1234", aircraft=aircraft_instance)

"""


class Flight:
    """A flight with a specific passenger aircraft.

    Attributes:
        _number (str): The flight number.
        _aircraft (Aircraft): The aircraft associated with the flight.

    """

    def __init__(
        self, number, aircraft
    ):  # class initialisation; automatically called when an instance of the class is created
        """Initialize a Flight instance.

        Args:
            number (str): The flight number.
            aircraft (Aircraft): The aircraft associated with the flight.

        Raises:
            ValueError: If the format of the flight number is invalid.

        """
        # Check the format of the flight number to create an invariant (error) check 
        if not (number[:2].isalpha()):  # adhoc check
            raise ValueError(
                f"Invalid 2 airline code (character), check case in '{number}'"
            )

        if not (number[:2].isupper()):
            raise ValueError(
                f"Invalid 2 airline code (MAJ char), check case in '{number}'"
            )

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid airline code (digit), check case in '{number}'")

        # Assign the validated flight number to the instance variable _number
        self._number = number
        # Create a friend (Law of Demetre) to accept an _aircraft object when it is constructed
        self._aircraft = aircraft
        # Retrieve the seat and rows numbers usning tuple unpacking
        rows, seats = self._aircraft.seating_plan()
        # Allocate the seats by concatenating the list of rows retrieved from Aircraft seating plan ie (range(1, 11), 'ABC')
        self._seating = [None]  + [{letter: None for letter in seats} for _ in rows]    # None is a single waste element to allign the numbering with 1 ; _ discard the row and focus on the letter

    def aircraft_model(self):
        """Get the model of the associated aircraft.

        Returns:
            str: The model of the aircraft.

        """
        # Getter method for retrieving the aircraft model from the Aircraft Class
        return self._aircraft.model()

    def number(self):
        """Get the flight number.

        Returns:
            str: The flight number.

        """
        # Getter method for retrieving the flight number
        return self._number

    def airline(self):
        """Get the airline code.

        Returns:
            str: The airline code (first two characters of the flight number).

        """
        # Getter method for retrieving the airline code (first two characters of the flight number)
        return self._number[:2]

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger.

        Args:
            seat (str): A seat designator such as '10B' or 3A.
            passenger (str): The passenger name.

        Raises:
            ValueError: If the seat (seat letter or row number) is incorrect or occupied.
        """
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:  # check the seat is not occupied using an identity check with 'None'
            raise ValueError(f"Seat {seat} already occupied")

        self._seating[row][letter] = passenger      # after validation, if row and seat unoccupied asssign seat

    def _parse_seat(self, seat):
        """Parse the seat designator into row and seat letter.

        Args:
            seat (str): A seat designator such as '10B' or 3A.

        Returns:
            tuple: A tuple containing the row number (int) and seat letter (str).

        Raises:
            ValueError: If the seat designation is incorrect.
        """
        rows, seat_letters = self._aircraft.seating_plan()

        # Extract seat letter and row number from the provided seat designator.
        letter = seat[-1]               # collect all the seat letters
        if letter not in seat_letters:  # validate its correctness
            raise ValueError(f"Invalid seat letter {letter}")

        row_text = seat[:-1]            # slice the row and get all the characters but not the last
        try:
            row = int(row_text)         # get the row in text and use it as a reference for the error is any
        except ValueError as e:
            raise ValueError(f"Invalid seat number {row_text}") from e

        if row not in rows:             # validate the row number with an in operation in the row range
            raise ValueError(f"Invalid row number {row}")

        return rows, letter

    def relocate_passenger(self, from_seat, to_seat):
        """Relocate a passenger to a different seat.

        Args:
            from_seat (str): The seat to relocate from.
            to_seat (str): The seat to relocate to.

        Raises:
            ValueError: No passenger to relocate or seat already occupied.
        """
        from_row, from_letter = self._parse_seat(from_seat)     # check if a variable contains a seat to relocate
        if self._seating[from_row][from_letter] is not None:
            raise ValueError(f"No passenger to relocate in seat{from_seat}")

        to_row, to_letter = self._parse_seat(to_seat)           # check if a seat is already allocated
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f"Seat {to_seat} already occupied by {from_seat}")

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter] # relocate the seat
        self._seating[from_row][from_letter] = None                             # reset the relocator variables, from_row and from_letter

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None) 
                   for row in self._seating
                   if row is not None) 

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        """An iterable series of passenger seating allocations."""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, f"{row}{letter}")


class Aircraft:
    """A base class representing an aircraft.

    Attributes:
        _registration (str): The registration number of the aircraft.
    """

    def __init__(self, registration):
        """Initialize an Aircraft instance.

        Args:
            registration (str): The registration number of the aircraft.
        """
        self._registration = registration

    def registration(self):
        """Get the registration number of the aircraft.

        Returns:
            str: The registration number.
        """
        return self._registration

    def num_seats(self):
        """Calculate the total number of seats in the aircraft.

        Returns:
            int: The total number of seats.
        """
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


class AirbusA319(Aircraft):
    """A specific type of aircraft - Airbus A319.

    Inherits from Aircraft class.

    Methods:
        model(): Get the model of the Airbus A319.
        seating_plan(): Get the seating plan of the Airbus A319.

    """

    def model(self):
        """Get the model of the Airbus A319.

        Returns:
            str: The model of the aircraft.
        """
        return "Airbus A319"

    def seating_plan(self):
        """Get the seating plan of the Airbus A319.

        Returns:
            tuple: A tuple containing the range of row numbers and a string of seat labels.
        """
        return range(1, 23), "ABCDEF"


class Boeing777(Aircraft):
    """A specific type of aircraft - Boeing 777.

    Inherits from Aircraft class.

    Methods:
        model(): Get the model of the Boeing 777.
        seating_plan(): Get the seating plan of the Boeing 777.

    """

    def model(self):
        """Get the model of the Boeing 777.

        Returns:
            str: The model of the aircraft.
        """
        return "Boeing 777"

    def seating_plan(self):
        """Get the seating plan of the Boeing 777.

        Returns:
            tuple: A tuple containing the range of row numbers and a string of seat labels.
        """
        # For simplicity's sake, we ignore complex seating arrangement for first-class
        return range(1, 56), "ABCDEGHJK"


def card_printer(passenger, seat, flight_number, aircraft):
    """Print a boarding card for a passenger.

    Args:
        passenger (str): The passenger's name.
        seat (str): The seat number.
        flight_number (str): The flight number.
        aircraft (str): The aircraft model.
    """
    output = (
        f"| Name: {passenger}"
        f"  Flight: {flight_number}"
        f"  Seat: {seat}"
        f"  Aircraft: {aircraft}"
        f" |"
    )
    banner = '+' + '-' * (len(output) - 2) + '+'
    border = '|' + ' ' * (len(output) - 2) + '|'
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()


def make_flights():
    """Create and return instances of Flight with Airbus A319 and Boeing 777.

    Returns:
        tuple: Two Flight instances with different aircraft types.
    """
    f = Flight("BA758", AirbusA319("G-EUPT"))
    f.allocate_seat("12A", "Guido van Rossum")
    f.allocate_seat("15F", "Bjarne Stroustrup")
    f.allocate_seat("15E", "Anders Hejlsberg")
    f.allocate_seat("1C", "John McCarthy")
    f.allocate_seat("1D", "Richard Hickey")

    g = Flight("AF72", Boeing777("F-GSPS"))
    g.allocate_seat('55K', 'Larry Wall')
    g.allocate_seat('33G', 'Yukihiro Matsumoto')
    g.allocate_seat('4B', 'Brian Kernighan')
    g.allocate_seat('4A', 'Dennis Ritchie')

    return f, g
