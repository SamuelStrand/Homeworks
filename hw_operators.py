# class Circle:
#     def __init__(self, diameter):
#         self.radius = diameter / 2
#         self.c = 2 * 3.14 * self.radius
#
#     def __eq__(self, other):
#         return self.radius == other.radius
#
#     def __lt__(self, other):
#         return self.c < other.c
#
#     def __le__(self, other):
#         return self.c <= other.c
#
#     def __add__(self, other):
#         return self.radius + other.radius
#
#     def __sub__(self, other):
#         return self.radius - other.radius
#
#     def __iadd__(self, other):
#         self.radius = self.radius + other.radius
#         return self.radius
#
#     def __isub__(self, other):
#         self.radius = self.radius - other.radius
#         return self.radius
#
#
# class Complex:
#     def __init__(self, a, b, i):
#         self.a = a
#         self.b = b
#         self.i = i
#
#     def __add__(self, other):
#         self.i = other.i
#         num1 = self.a + self.b * self.i
#         num2 = other.a + other.b * self.i
#         return num1 + num2
#
#     def __sub__(self, other):
#         self.i = other.i
#         num1 = self.a + self.b * self.i
#         num2 = other.a + other.b * other.i
#         return num1 - num2
#
#     def __mul__(self, other):
#         self.i = other.i
#         num1 = self.a + self.b * self.i
#         num2 = other.a + other.b * other.i
#         return num1 * num2
#
#     def __truediv__(self, other):
#         self.i = other.i
#         num1 = self.a + self.b * self.i
#         num2 = other.a + other.b * other.i
#         return num1 / num2
#
#
# class Airplane:
#     def __init__(self, plane_type, passengers, delta):
#         self.plane_type = plane_type
#         self.passengers_delta = delta
#         self.passengers = passengers
#         self.max_passengers = delta + passengers
#
#     def __eq__(self, other):
#         return self.plane_type == other.plane_type
#
#     def __add__(self, other):
#         return self.passengers + self.passengers_delta
#
#     def __sub__(self, other):
#         return self.passengers - self.passengers_delta
#
#     def __iadd__(self, other):
#         self.passengers = self.passengers_delta + self.passengers
#         return self.passengers
#
#     def __isub__(self, other):
#         self.passengers = self.passengers_delta - self.passengers
#         return self.passengers
#
#     def __lt__(self, other):
#         return self.max_passengers < other.max_passengers
#
#     def __le__(self, other):
#         return self.max_passengers <= other.max_passengers
#
#
# class Flat:
#     def __init__(self, square):
#         self.square = square
#
#     def __eq__(self, other):
#         return self.square == other.square
#
#     def __ne__(self, other):
#         return self.square != other.square
#
#     def __le__(self, other):
#         return self.square <= other.square
#
#     def __ge__(self, other):
#         return self.square >= other.square
#
#     def __gt__(self, other):
#         return self.square > other.square


class Figure:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __int__(self):
        return self.square()

    def __str__(self):
        if self.square() == self.a * self.b:
            return 'Rectangle'
        if self.square() == 2 * self.a * self.b:
            return 'Circle'

    def square(self):
        square = self.a * self.a
        return square


class Rectangle(Figure):
    def __init__(self, a, b):
        super().__init__(a, b)

    def square(self):
        square = self.a * self.b
        return square


class Circle(Figure):
    def __init__(self, b, a=3.14):
        super().__init__(a, b)

    def square(self):
        square = 2 * self.a * self.b
        return int(square)


class Triangle(Figure):
    def __init__(self, a, b):
        super().__init__(a, b)

    def square(self):
        return int(0.5 * self.a * self.b)


class Trapezoid(Figure):
    def __init__(self, a, b, h):
        self.h = h
        super().__init__(a, b)

    def square(self):
        return int((self.a + self.b) / 2 * self.h)


obj = Rectangle(3, 5)
obj2 = Circle(b=5)
obj3 = Trapezoid(2, 5, 4)


print(str(obj))

if __name__ == '__main__':
    # circle1 = Circle(10)
    # circle2 = Circle(15)
    # print(circle1 - circle2)

    # num3 = Complex(1, 3, 2)
    # num4 = Complex(4, 5, 2)
    # print(num3 / num4)

    # plane1 = Airplane('Type1', passengers=50, delta=30)
    # plane2 = Airplane('Type2', passengers=20, delta=30)
    # print(plane1 >= plane2)
    # print(plane1 + 'more passengers')
    # print(plane1 - 'less passengers')
    # flat1 = Flat(60)
    # flat2 = Flat(55)
    #
    # print(flat1 < flat2)
