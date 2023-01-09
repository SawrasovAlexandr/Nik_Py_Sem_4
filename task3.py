# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

# def simple_div(number):
#     result = []
#     div = 2
#     while number != 1:
#         if 

a, b = int(input('Введите a')), int(input('Введите b'))
max_num = max(a, b)
for i in range(max_num, (a * b) + 1, max_num):
    if i % a == i % b == 0:
        print(i)
        break
