# TASK 4
def task4():
    print(""""Don't compare yourself with anyone in this world…
    if you do so, you are insulting yourself.”
    Bill Gates
     """)


# TASK 5
def task5(num1: int, num2: int):
    arr = []
    for i in range(num1, num2):
        arr.append(i)
    return arr[num1:num2:2]


# TASK 6

def task6(length, symbol, boolean: bool):
    side1 = symbol * length
    if not boolean:
        side2 = symbol + " " * (length - 2) + symbol
    else:
        side2 = side1
    print(side1)
    for i in range(length - 2):
        print(side2)
    print(side1)


# TASK 7

def task7(num1, num2, num3, num4, num5):
    smallest = num1
    if smallest > num2:
        smallest = num2
        return smallest
    if smallest > num3:
        smallest = num3
        return smallest
    if smallest > num4:
        smallest = num4
        return smallest
    if smallest > num5:
        smallest = num5
        return smallest
    else:
        smallest = num1
        return smallest


# TASK 8


def task8(range1: int, range2: int) -> int:
    if range1 < range2:
        total = 1
        for i in range(range1, range2 + 1):
            total *= i
        return total
    elif range1 > range2:
        total = 1
        for i in range(range2, range1 + 1):
            total *= i
        return total


# TASK 9

def task9(num: int) -> int:
    index = 0
    for i in str(num):
        index += 1
    return index


# TASK 10

def task10(palindrome):
    word = str(palindrome).lower().replace(' ', '')
    if word == word[::-1]:
        return 'Палиндром'
    else:
        return 'Не палиндром'


if __name__ == '__main__':
    task4()
    print(task5(1, 10))
    task6(5, '#', True)
    print(task7(10, 20, 30, 40, 50))
    print(task8(4, 6))
    print(task9(3456))
    print(task10('123321'))
