from random import randint


class CountRoomsException(Exception):
    pass


class House:
    def __init__(self, address, owner, apartments_count, floors, built_year, house_name, entrances, base_price,
                 entrance_square_lim, min_rooms, max_rooms):
        self.address = address
        self.owner = owner
        self.apartments_count = apartments_count
        self.floors = floors
        self.built_year = built_year
        self.house_name = house_name
        self.entrances = entrances
        self.base_price = base_price
        self.entrance_square_lim = entrance_square_lim
        self.min_rooms = min_rooms
        self.max_rooms = max_rooms
        self.total_square = entrances * floors * entrance_square_lim
        self.apartments = []

    def fill_apartments(self):
        apartment_numeration = 1
        for floor in range(1, self.floors + 1):
            for entrance in range(1, self.entrances + 1):
                free_square = self.entrance_square_lim
                while True:

                    rooms = randint(self.min_rooms, self.max_rooms)
                    square = self.get_square(rooms)
                    apartment = Apartment(rooms=rooms, apart_number=apartment_numeration, square=square,
                                          floor=floor, entrance=entrance, house=self)

                    if free_square > 0 and free_square >= square:
                        self.apartments.append(apartment)
                        apartment_numeration += 1
                        free_square -= square
                    elif free_square == 0:
                        break
                    print(f"Floor{floor}, entrance:{entrance}, free_square:{free_square},square:{square}")

        print(apartment_numeration)

    def get_square(self, rooms):
        if rooms == 1:
            square = (randint(20, 40) // 20) * 20
        elif rooms == 2:
            square = (randint(40, 80) // 20) * 20
        elif rooms == 3:
            square = (randint(80, 120) // 20) * 20
        elif rooms == 4:
            square = (randint(120, 160) // 20) * 20
        else:
            raise CountRoomsException("В цьому будинку є тільки 4 кімнати!")

        return square

    def calculate_total_square(self):
        return sum([apartment.square for apartment in self.apartments])


class Apartment:
    def __init__(self, rooms, apart_number, square, floor, entrance, house: House):
        self.rooms = rooms
        self.apart_number = apart_number
        self.square = square
        self.floor = floor
        self.entrance = entrance
        self.house = house
        self.price = None

    def get_apartment_price(self):
        self.price = self.house.base_price * self.square
        return f"Apartment price is: {self.price}"

    def __repr__(self):
        return f"Apartment info: {self.rooms},{self.apart_number},{self.square},{self.floor},{self.entrance},{self.price}"


house1 = House('Haeftenzeile 11', 'Illia', 100, 4, 2000, 'Illia Castle',
               4, 2000, 600, 1, 4)

house1.fill_apartments()

print(house1.apartments)

print(house1.total_square)
print(house1.calculate_total_square())
apartments_wiht_price = [apartment.get_apartment_price() for apartment in house1.apartments]
print(house1.apartments)
