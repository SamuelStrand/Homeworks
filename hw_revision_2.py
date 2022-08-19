# Task 1
print('Task 1')

user_day = int(input('Введите номер дня недели: '))
if user_day == 1:
    print('Понедельник')
elif user_day == 2:
    print('Вторник')
elif user_day == 3:
    print('Среда')
elif user_day == 4:
    print('Четверг')
elif user_day == 5:
    print('Пятница')
elif user_day == 6:
    print('Суббота')
elif user_day == 7:
    print('Воскресенье')
else:
    print('Number is out of range')

# Task2
print('\n')
print('Task 2')

user_month = int(input('Введите номер месяца: '))
if user_month == 1:
    print('Январь')
elif user_month == 2:
    print('Февраль')
elif user_month == 3:
    print('Март')
elif user_month == 4:
    print('Апрель')
elif user_month == 5:
    print('Май')
elif user_month == 6:
    print('Июнь')
elif user_month == 7:
    print('Июль')
elif user_month == 8:
    print('Август')
elif user_month == 9:
    print('Сентябрь')
elif user_month == 10:
    print('Октябрь')
elif user_month == 11:
    print('Ноябрь')
elif user_month == 12:
    print('Декабрь')
else:
    print('Number is out of range')


# Task 3
print('\n')
print('Task 3')

user_number = int(input('Введите число: '))

if user_number > 0:
    print('Number is positive')
elif user_number < 0:
    print('Number is negative')
elif user_number == 0:
    print('Number is equal to zero')

# Task 4
print('\n')
print('Task 4')

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второче число: '))

if first_number == second_number:
    print('The numbers are equal')
elif first_number < second_number:
    print(first_number, second_number)
elif second_number < first_number:
    print(second_number, first_number)

# Task 5
print('\n')
print('Task 5')

first_num_of_range = int(input('Enter the first number of range: '))
last_num_of_range = int(input('Enter the last number of range: '))

user_range = range(first_num_of_range, last_num_of_range+1)
for i in user_range:
    if i % 7 == 0:
        print(i)

# Task 6
print('\n')
print('Task 6')

first_num_of_range = int(input('Enter the first number of range: '))
last_num_of_range = int(input('Enter the last number of range: '))

user_range = range(first_num_of_range, last_num_of_range+1)
for i in user_range:
    print(i)

print('\n#################\n')

for i in user_range[::-1]:
    print(i)

print('\n#################\n')

for i in user_range:
    if i % 7 == 0:
        print(i)

print('\n#################\n')

n = 0

for i in user_range:
    if i % 5 == 0:
        n += 1
print(n)

# Task 7
print('\n')
print('Task 7')

first_num_of_range = int(input('Enter the first number of range: '))
last_num_of_range = int(input('Enter the last number of range: '))

user_range = range(first_num_of_range, last_num_of_range+1)

for i in user_range:
    if i % 3 == 0 and i % 5 == 0:
        print('Fizz Buzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)


