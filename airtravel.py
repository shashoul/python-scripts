"""Model for aircraft flights."""

class Flight:
    """A flight with a particular passenger aricraft."""
    
    def __init__(self, number, aircraft):
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter : None for letter in seats} for _ in rows]


    def number(self):
        return self._number


    def aircraft(self):
        return self._aircraft.model()


    def allocate_seat(self, seat, passenger):
        row , letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError(f"This seat {letter} Already occupied")
        
        self._seating[row][letter] = passenger
            

    def relocate_passenger(self, from_seat, to_seat):
        from_row , from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"from seat {from_seat} is not occupied!!")
        
        to_row , to_seat = self._parse_seat(to_seat)
        if self._seating[to_row][to_seat] is not None:
            raise ValueError(f"to seat {to_seat} is occupied!!")
        
        self._seating[to_row][to_seat] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None


    def _parse_seat(self, seat):
        row = int(seat[:-1])
        letter = seat[-1]

        rows, seats = self._aircraft.seating_plan()

        if row not in rows:
            raise ValueError(f"{row} not exist in Aircraft")
        
        if letter not in seats:
            raise ValueError(f"{letter} not exist in Aircraft seats")

        return (row,letter)


    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None) 
                            for row in self._seating if row is not None)

class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row


    def registration(self):
        return self._registration


    def model(self):
        return self._model


    def seating_plan(self):
        return (range(1,self._num_rows+1),
                "ABCDEFGHJ"[:self._num_seats_per_row])

