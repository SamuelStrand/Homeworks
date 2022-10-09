from flask import Flask
from random import randint

list1 = [randint(1, 666) for x in range(1, 666)]

sorted_list = []


def sort_bubble(list_ran: list, is_revers=False) -> list:
    len1 = len(list_ran)
    for i in range(0, len1):
        for j in range(0, len1 - 1 - i):
            if is_revers:
                if list_ran[j] < list_ran[j + 1]:
                    list_ran[j], list_ran[j + 1] = list_ran[j + 1], list_ran[j]
            else:
                if list_ran[j] > list_ran[j + 1]:
                    list_ran[j], list_ran[j + 1] = list_ran[j + 1], list_ran[j]
    global sorted_list
    sorted_list = list_ran
    return sorted_list


print(sort_bubble(list1, is_revers=False))

app = Flask(__name__)


@app.route("/sorted_list")
def return_sorted_list():
    return sorted_list


@app.route("/")
def hello_world():
    return 'hello world'
