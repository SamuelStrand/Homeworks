# Task 1
print('Task 1')

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите число число: '))

summary = a + b + c
print(f'Сумма: {summary}')
multiply = a * b * c
print(f'Произведение: {multiply}')

# Task2
print('\n')
print('Task 2')

salary = int(input('Введите вашу зарплату: '))
loan = int(input('Введите вашу сумму месячного платежа по кредиту в банке: '))
utility_bills = int(input('Введите вашу задолженность по коммунальным услугам: '))

money_after_all_payments = salary - (loan + utility_bills)
print(f'У вас осталось: {money_after_all_payments}')

# Task 3
print('\n')
print('Task 3')

d1 = int(input('Первая диагональ ромба: '))
d2 = int(input('Вторая диагональ ромба: '))

s = (d1*d2)/2
print(f'Площадь равна {s}')

# Task 4
print('\n')
print('Task 4')

print('to be')
print('or not')
print('to be')

# Task 5
print('\n')
print('Task 5')

print('“Life is what happens')
print('when')
print('you’re busy making other plans”')
print('John Lennon')

# Task 6
print('\n')
print('Task 6')

a = (input('Введите первое число: '))
b = (input('Введите второе число: '))
c = (input('Введите число число: '))

summary = a + b + c
print(f'Сумма: {summary}')

# Task 7
print('\n')
print('Task 7')

seven_task_num = input('Введите четырех значное число: ')
sum_of_numbers = int(seven_task_num[0]) * int(seven_task_num[1]) * int(seven_task_num[2]) * int(seven_task_num[3])
print(sum_of_numbers)

# Task 8
print('\n')
print('Task 8')

meters = int(input('Введите метры: '))
sm = meters * 100
dm = meters * 10
mm = meters * 1000
mils = meters * 0.000621371
print(f'Сантиметры: {sm}')
print(f'Дециметры: {dm}')
print(f'Миллиметры: {mm}')
print(f'Мили: {mils}')

# Task 9
print('\n')
print('Task 9')

a_side = int(input('Сторона треугольника: '))
h = int(input('Высота треугольника: '))

s_triangle = 0.5 * a_side * h

print(f'Площадь треугольника: {s_triangle}')

# Task 10
print('\n')
print('Task 10')

user_number = input('Введите четырехзначное число: ')
print(user_number[::-1])
