import pprint as pp

# pp.pprint('ala')


class Flight:
    def __init__(self, flight_number, aircraft):
        self.flight_number = flight_number
        self.aircraft = aircraft

        rows, seats = self.aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def get_airline(self):
        return self.flight_number[:2]

    def get_number(self):
        return self.flight_number[2:]

    def aircraft_model(self):
        return self.aircraft.get_model()

    def _parse_seat(self, seat):
        row_numbers, seat_letters = self.aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f'Invalid seat letter {letter}')

        row_text = seat[:-1]


        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f'Invalid row number {row_text}')

        if row not in row_numbers:
            raise ValueError(f'No correct row number my {row}')

        return row, letter

    def allocate_seat(self, seat='12C', passenger="Mateusz M"):
        row, letter =self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError(f'Seat {seat} already occupied ')

        self._seating[row][letter] = passenger

        #TODO homework
    def relocate_seat(self, from_seat, to_seat):
        pass

    def num_available_seats(self):
        return sum(sum(1 for seat in row.values() if seat is None)
                   for row in self._seating
                   if row is not None)

    def make_boarding_cards(self, card_printer):
        for passenger, seat in self._passenger_seat():
            card_printer(passenger, seat, self.flight_number, self.aircraft_model())

    def _passenger_seat(self):
        row_numbers, seat_letters = self.aircraft.seating_plan()

        for row in row_numbers:
            for seat_letters in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    # yield to return na po - wywołując go tyle razy ile jest elementów zawsze zwraca kolejny
                    yield (passenger, f'{row}{letter}')


class Aircraft:
    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)




class AirbusA319(Aircraft):

    def get_model(self):
        return 'Airbus A319'

    def seating_plan(self):
        return range(1, 23), 'ABCDEF'


#TODO
def console_card_printer(passenger, seat, flight_number, aircraft):
    # Zrobić piękny wydruk ze ślaczkami
    # frame_1 = f'+ {"-"*200}+'
    # print(frame_1)
    # frame = f'+{"-" * (len(name) + 2)}+'
    # text = f'| {name} |'
    # list_of_lines = [frame, frame, frame, text, frame, frame, frame]
    # output = '\n'.join(list_of_lines)
    # print(output)
    pass


airbus = AirbusA319()
# print(airbus.num_seats())
f = Flight('LO234', airbus)
# print(f.aircraft_model())
# print(f.get_airline())
# print(f.get_number())

print(f.num_available_seats())
f.allocate_seat('10A', 'Jarosław K')
f.allocate_seat('10B', 'Lech K')
f.allocate_seat('10C', 'Mateusz M')
# pp.pprint(f._seating)
print(f.num_available_seats())
# f.make_boarding_cards(console_card_printer)
console_card_printer("x","23","fd","34")






