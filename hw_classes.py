class Car:
    def __init__(self, model: str, release_year: int, manufacturer: str, engine_volume: float, color: str,
                 price: float):
        self.model = model
        self.release_year = release_year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def model(self):
        return self.model

    def release_year(self):
        return self.release_year

    def how_old_is_car(self, current_year=2022):
        return current_year - self.release_year

    def manufacturer(self):
        return self.manufacturer

    def engine_volume(self):
        return self.engine_volume

    def color(self):
        return self.color

    def price(self):
        return self.price

    def change_model(self):
        self.model = input('Enter your car model: ')


class Book:
    def __init__(self, name: str, release_year: int, production: str, genre: str, author: str, price: float):
        self.name = name
        self.release_year = release_year
        self.production = production
        self.genre = genre
        self.author = author
        self.price = price

    def name(self):
        return self.name

    def release_year(self):
        return self.release_year

    def how_old_is_book(self, current_year=2022):
        return current_year - self.release_year

    def production(self):
        return self.production

    def genre(self):
        return self.genre

    def author(self):
        return self.author

    def price(self):
        return self.price


class Stadium:
    def __init__(self, name: str, opening_year: int, country: str, city: str, capacity: int):
        self.name = name
        self.opening_year = opening_year
        self.country = country
        self.city = city
        self.capacity = capacity

    def name(self):
        return self.name

    def opening_year(self):
        return self.opening_year

    def how_old_is_stadium(self, current_year=2022):
        return current_year - self.opening_year

    def country(self):
        return self.country

    def city(self):
        return self.city

    def capacity(self):
        return self.capacity

    def are_any_free_seats(self, present_people):
        return f'{self.capacity - present_people} seats are available'


if __name__ == '__main__':
    cars = Car('Toyota', 2007, 'China', 2.5, 'red', 2000)
    print(cars.model)
    print(cars.how_old_is_car(2022))
    print(cars.change_model())
    print(cars.model)

    book = Book(name='Piece and war', release_year=1865, production='something', genre='novel', author='L.N. Tolstoy',
                price=100)
    print(book.how_old_is_book(2022))

    stadium = Stadium(name='Stadium', opening_year=1999, country='Kazakhstan', city='Almaty', capacity=60000)
    print(stadium.how_old_is_stadium())
    print(stadium.are_any_free_seats(46321))
