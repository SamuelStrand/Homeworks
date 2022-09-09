class Car:
    def __init__(self, model, release_year, manufacturer, engine_volume, color, price):
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

    def manufacturer(self):
        return self.manufacturer

    def engine_volume(self):
        return self.engine_volume

    def color(self):
        return self.color

    def price(self):
        return self.price


cars = Car('Toyota', 2007, 'China', 2.5, 'red', 2000)
print(cars.model)

