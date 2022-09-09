request_from_user1 = {
    "url": "localhost/home/",
    "method": "PUT",
    "data": {"попытка входа": 1},
    "timeout": 3000,
    "headers": {
        "Authorization": 'Bearer admin qwerty12345',
    },
}

request_from_user2 = {
    "url": "localhost/",
    "method": "123",
    "data": {"попытка входа": 1},
    "timeout": -1,
    "headers": {},
}

headers1 = request_from_user1['headers']
headers2 = request_from_user2['headers']

user_input_login_and_password = request_from_user1["headers"]["Authorization"]
incorrect_login_and_password = False


# TASK 2
def checking_data(function):
    def wrapper(request, header=1):
        function(request)
        try:
            if header == 1 and headers1:
                return 'headers are alright'
            elif not headers1:
                return 'problem with headers'
            elif header == 2 and headers2:
                return 'headers are ok'
            elif not headers2:
                return 'problem with headers'

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
        if user_input_login_and_password != incorrect_login_and_password:
            print(auth.check_auth())
        else:
            raise AuthError(exception_text="incorrect login")
    except AuthError as error:
        error = error.return_error()
        print(error)


# TASK 3
class RequestManager:
    def __init__(self, request):
        self.request = request

    def check_method(self):
        if self.request['method'] not in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']:
            return 'Error! Invalid method'
        else:
            return 'Methods are ok'

    def check_timeout(self):
        if self.request['timeout'] <= 0:
            return 'Error! Problem with timeout'
        else:
            return 'Timeout are ok'

    def check_auth(self):
        if self.request['headers']:
            return 'Auth data is ok'
        else:
            return 'Problem with authorisation'


# TASK 4
class Help:
    def __init__(self, number_pi=3.14159265359):
        self.number_pi = number_pi

    @staticmethod
    def convert_to_string(value) -> str:
        return str(value)

    def find_square_of_circle(self, radius: float) -> float:
        square = self.number_pi * (radius ** 2)
        return square

    def find_circumference(self, radius: float) -> float:
        c = 2 * self.number_pi * radius
        return c


methods = RequestManager(request=request_from_user1)
timeout = RequestManager(request=request_from_user1)
auth = RequestManager(request=request_from_user1)
obj = Help()

if __name__ == '__main__':
    print(check_user_request(request=request_from_user1, header=1))
    print(methods.check_method())
    print(timeout.check_timeout())

    print(f'Ваша строка: {obj.convert_to_string(True)}')
    print(f'Площадь круга равна: {obj.find_square_of_circle(radius=10)}')
    print(f'Длина окружности равна: {obj.find_circumference(radius=5)}')
