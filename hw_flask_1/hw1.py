from flask import Flask, render_template
from random import randint

list1 = [randint(1, 666) for x in range(1, 666)]

sorted_list = []


def sort_bubble(list_ran: list, is_revers=False) -> list:
    len1 = len(list_ran)
    for i in range(0, len1):
        for j in range(0, len1 - 1 - i):
            if is_revers:
                if list_ran[j] < list_ran[j + 1]:
                    # temp_i = list_ran[i]
                    # list_ran[i] = list_ran[i + 1]
                    # list_ran[i+1] = temp_i
                    list_ran[j], list_ran[j + 1] = list_ran[j + 1], list_ran[j]
            else:
                if list_ran[j] > list_ran[j + 1]:
                    list_ran[j], list_ran[j + 1] = list_ran[j + 1], list_ran[j]
    global sorted_list
    sorted_list = list_ran
    return sorted_list


print(sort_bubble(list1, is_revers=False))

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('hw1.html')
