request_from_user1 = {
    "url": "localhost/home/",
    "method": "GET",
    "data": {"попытка входа": 1},
    "timeout": 3000,
    "headers": {
        "Authorization": 'Bearer admin qwerty12345',
    },
}

request_from_user2 = {
    "url": "localhost/",
    "method": "POST",
    "data": {"попытка входа": 1},
    "timeout": 3000,
    "headers": {},
}

headers1 = request_from_user1['headers']
headers2 = request_from_user2['headers']

user_input_login_and_password = request_from_user1["headers"]["Authorization"]
incorrect_login_and_password = False


# TASK 2
def checking_data(function):
    def wrapper():
        function()
        try:
            if headers2:
                print('Headers are alright')
            else:
                raise AuthError(exception_text="no headers lol")
        except AuthError as headers_error:
            headers_error = headers_error.empty_headers()
            print(headers_error)

    return wrapper


# TASK 1

class AuthError(Exception):
    def __init__(self, exception_text: str):
        self.exception_text = exception_text

    def return_error(self):
        return f'ATTENTION! AN ERROR HAS OCCURRED: {self.exception_text}'

    def empty_headers(self):
        return 'Empty headers!!!'


@checking_data
def check_user_request(request):
    try:
        if user_input_login_and_password == incorrect_login_and_password:
            return RequestManager(request)
        else:
            raise AuthError(exception_text="incorrect login")
        return 'Error'
    except AuthError as error:
        error = error.return_error()
        print(error)



# TASK 3
class RequestManager:
    def __init__(self, request):
        self.request = request

    def check_method(self):
        if self.request['method'] not in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']:
            raise Exception

        if headers2:
            print('Headers from the second request are ok')
        else:
            print('Incorrect headers from the second request')


request_from_user1 = RequestManager()
request_from_user1.check_method()

# TASK 4
# class Help:
#     def __init__(self, number_pi=3.14159265359):
#         self.number_pi = number_pi
#
#     @staticmethod
#     def convert_to_string(value) -> str:
#         return str(value)
#
#     def find_square_of_circle(self, radius: float) -> float:
#         square = self.number_pi * (radius ** 2)
#         return square
#
#     def find_circumference(self, radius: float) -> float:
#         c = 2 * self.number_pi * radius
#         return c
#
#
# obj = Help()
# print(f'Ваша строка: {obj.convert_to_string(True)}')
# print(f'Площадь круга равна: {obj.find_square_of_circle(radius=10)}')
# print(f'Длина окружности равна: {obj.find_circumference(radius=5)}')


if __name__ == '__main__':
    check_user_request()
