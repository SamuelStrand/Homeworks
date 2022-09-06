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

user_input_login_and_password = request_from_user1["headers"]["Authorization"]
correct_login_and_password = request_from_user1["headers"]["Authorization"]
incorrect_login_and_password = False


class AuthError(Exception):
    def __init__(self, exception_text: str):
        self.exception_text = exception_text

    def return_error(self):
        return f'ATTENTION! AN ERROR HAS OCCURRED: {self.exception_text}'


def check_user_request():
    try:
        if user_input_login_and_password != correct_login_and_password:
            pass
        else:
            raise AuthError(exception_text="incorrect login")
        return 'Error'
    except AuthError as error:
        error = error.return_error()
        print(error)


print(check_user_request())
