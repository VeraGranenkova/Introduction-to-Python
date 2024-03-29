# Задача № 1
# Возведение в степень
# Напишите функцию f, которая на вход принимает два числа a и b,
# и возводит число a в целую степень b с помощью рекурсии.
# Функция не должна ничего выводить, только возвращать значение.

# Пример:

# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8 

# Вариант 1
# a = 3
# b = 5

# def f(a,b):
#     if b == 1:
#         return a
#     return a * f(a, b - 1)
# print(f(a, b))

# Вариант 2
# a = 3
# b = 5
# def f(a, b):
#   if b == 0:
#     return 1
#   return f(a, b - 1) * a
# print(f(a, b))


# Задача № 2
# Рекурсивная сумма
# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# Функция не должна ничего выводить, только возвращать значение.

# Пример:

# sum(2, 2)
#  4

# Вариант 1
# a = 3
# b = 5
# def sum(a, b):
#     if b == 0:
#         return a
#     if a == 0:
#         return b
#     return sum(a + 1, b - 1)
# print(sum(a, b))

# Вариант 2
# a = 3
# b = 5
# def sum(a, b):
#     if b == 0:
#         return a
#     elif a == 0:
#         return b
#     else:
#         return sum(a + 1, b - 1)
# print(sum(a, b))
