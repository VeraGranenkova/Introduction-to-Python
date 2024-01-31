# Задача №39.  
# 1) Даны два массива чисел. Требуется вывести те элементы первого
# массива (в том порядке, в каком они идут в первом массиве),
# которых нет во втором массиве. Пользователь вводит  число N - количество
# элементов в первом массиве, затем N чисел - элементы массива.
# Затем число M - количество элементов во втором массиве.
# Затем элементы второго массива

# 2) (пользовательский ввод можно заменить на рандомный ввод)
# Пользователь вводит  размер первого массива – N
# и элементы первого массива. 
# затем размер второго массива M  
# и элементы второго массива
# Нужно вывести те элементы первого массива,
# которых нет во втором массиве, при этом порядок последовательности
# сохранить исходный
# Ввод: 			
# 7			
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1
# Вывод:
# 3 3 2 12


# from random import randint

# n = int(input('Введите длинну 1го массива:'))
# m = int(input('Введите длинну 2го массива:'))

# # list1 = []
# # list2 = []


# # for _ in range(n):
# #     list1.append(randint(1, 10))
# list1 = [randint(1, 50) for _ in range(n)]
# print(list1)

# # for _ in range(m):
# #     list2.append(randint(1, 10))
# set2 = {randint(1, 50) for _ in range(m)}
# print(set2)

# # res_list = []

# # for num in list1:
# #     if num not in set2:
# #         res_list.append(num)
# #         print(num, end=' ')
# res_list = [num for num in list1 if num not in set2]

# # res_list = [num if num not in set2 else 0 for num in list1 ]

# print()
# print(*res_list)


# Задача №41.  
# 1) Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном массиве выведет количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного.
# Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел. 
# 2) (пользовательский ввод можно заменить на рандомный)
# Пользователь вводит  размер массива – N и элементы массива (целые числа).
# Нужно из этого массива вывести количество элементов,
# у которых ближайшие соседние элементы меньше самого элемента.

# Ввод: 			Ввод:
# 5			    5
# 1 2 3 4 5	    1 5 1 5 1

# Вывод:			Вывод:
# 0			    2


# import random

# n = int(input('введите размер списка: '))
# list_num = [random.randint(1, 5) for _ in range(n)]
# print(list_num)

# count = 0
# for i in range(1, len(list_num)-1):
#     if list_num[i-1] < list_num[i] > list_num[i+1]:
#         count += 1
# print(count) 

# # print(sum([1 for i in range(1, len(list_num)-1) if list_num[i-1] < list_num[i] > list_num[i+1]]))


# Задача №43.  
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список чисел.
# Все числа списка находятся на разных строках.

# 2) (пользовательский ввод можно заменить на рандомный)
# Пользователь вводит  размер массива – N
# и элементы массива (целые числа). 
# нужно посчитать сколько повторений у каждого числа
# посчитанные числа можно посчитать повторно в паре с другими числами

# Ввод:			Вывод:
# 1 2 3 2 3 2 2 2		11


# # Вариант 1
# list1 = [1, 2, 3, 2, 3]
# count = 0

# for i in range(len(list1)):
#     for j in range(i+1, len(list1)):
#         if i != j and list1[i] == list1[j]:
#             count += 1

# print(count)

# # Вариант 2
# n = int(input("Введите размер списка: "))
# my_list = [randint(1, 3) for _ in range(n)]
# count = 0
# for i in range(len(my_list)-1):
#     count += my_list[i+1:].count(my_list[i])
# print(count)
# print(my_list)

# # Вариант 3
# from random import randint

# n = int(input("Введите размер списка: "))
# my_list = [randint(1,3) for _ in range(n)]
# count = 0
# for i in range(len(my_list)):
#     for j in range(i+1, len(my_list)):
#         if my_list[i] == my_list[j]:
#             count+=1
# print(count)


# Задача №45.  
# Два различных натуральных числа n и m называются дружественными,
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.
# Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 105.
# Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k.
# Пары необходимо выводить по одной в строке, разделяя пробелами.
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
# (пользовательский ввод можно заменить на рандомный)
# Пользователь вводит  натуральное число  – k
# В диапазоне от 0 до k нужно вывести все пары чисел N и M, в которых сумма делителей N равняется M, а сумма делителей M равняется N (число само на себя делить нельзя)
# Пары необходимо выводить по одной паре в строке, разделяя числа пробелами. Каждая пара выводится только один раз, без повторов. 

# Пример: Возьмём 2 числа 220 и 284. Найдём их делители 
# Делители 220 – (1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110)
# 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110  = 284
# Делители 284 – (1, 2, 4, 71, 142 )
# 1 + 2 + 4 + 71 + 142 = 220
# 			Ввод:			Вывод:
# 			300			220 284

# # Вариант 1 лектор
# k = int(input())
# list1 = list()

# for i in range(k):
#     summa = 0
#     for j in range(1, i//2 + 1):
#         if i % j == 0:
#             summa += j
#     list1.append(tuple([i, summa]))

# for i in range(len(list1)):
#     for j in range(i, len(list1)):
#         if i != j and list1[i][0] == list1[j][1] and list1[i][1] == list1[j][0]:
#             print(*list1[i])

# # Вариант 2
# def sum_div(num):
#     summa = 1
#     for div in range(2, num):
#         if num % div == 0:
#             summa += div
#     return  summa   
#     #return sum(div for div in range(1, num) if num % div == 0)
# k = int(input('введите число: '))

# for num_1 in range(2, k + 1):
#     num_2 = sum_div(num_1)
#     if num_1 == sum_div(num_2) and num_1 < num_2:
#         print(num_1, num_2)

# # Вариант 3
# def sum_div(num):
#     summa = 1
#     for div in range(2, num // 2 + 1):
#         if num % div == 0:
#             summa += div
#     return  summa   
#     #return sum(div for div in range(1, num) if num % div == 0)
# k = int(input('введите число: '))

# for num_1 in range(2, k + 1):
#     num_2 = sum_div(num_1)
#     if num_1 < num_2 and num_1 == sum_div(num_2) and num_2 <= k:
#         print(num_1, num_2)

# # Вариант 4 оптимизированный
# def sum_div(num):
#     summa = 1
#     sq_num = num ** 0.5
#     int_q_num = int(sq_num)
#     if sq_num == int_q_num :
#         summa += int_q_num     
#     for div in range(2, int_q_num ):
#         if num % div == 0:
#             summa += div + num // div
#     return  summa   
# k = int(input('введите число: '))

# for num_1 in range(2, k + 1):
#     num_2 = sum_div(num_1)
#     if num_1 < num_2 and num_1 == sum_div(num_2) and num_2 <= k:
#         print(num_1, num_2)

