# import pprint as pp
# pp.pprint('ala')
from flight import Flight
from planes import *
from helpers import *


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
f.make_boarding_cards(console_card_printer)






