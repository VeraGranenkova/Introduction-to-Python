# Задача 1
# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.

# Пример:

# list_1 = [1, 2, 3, 4, 5]
# k = 3
# Вывод 1


# Вариант 1

# import random

# size = int(input("Введите размер списка: "))
# k = int(input("Введите число k: "))
# list_1 = [] 
# for _ in range(size):
#     num = random.randint(0, 10)
#     list_1.append(num)
# count = list_1.count(k)
# print(list_1)
# print(count)

# Вариант 2

# list_1 = [1, 2, 3, 4, 5]
# k = 3
# print(sum([1 for num in list_1 if num == k]))

# Вариант 3

# list_1 = [1, 2, 3, 4, 5]
# k = 3
# count = 0
# for num in list_1:
#     if num == k:
#         count += 1
# print(count)
# # print(list_1.count(k))


# Задача 2.
# Требуется найти в массиве list_1 самый близкий по значению элемент
# к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один.
# Если значение k совпадает с этим элементом - выведите его.

# Пример:

# list_1 = [1, 2, 3, 4, 5]
# k = 6
# 5

# Вариант 1
# sort_list = sorted(list_1)

# for i in range(len(sort_list)-1):
#     if k >= sort_list[-1]:
#         print(sort_list[-1])
#         break
#     if k <= sort_list[0]:
#         print(sort_list[0])
#         break
#     if sort_list[i] <= k <= sort_list[i + 1]:
#         if k - sort_list[i] >= sort_list[i + 1] - k:
#             print(sort_list[i + 1])
#             break
#         else:
#             print(sort_list[i])

# # Вариант 2

# m = abs(k - list_1[0])  # модуль числа
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)


# Задача 3

# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

# В случае с английским алфавитом очки распределяются так:

# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:

# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем
# слова k и выводит его. Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.

# Пример:

# k = 'ноутбук'
# # 12

# # Вариант 1
# # Пользователь вводит слово
# k = input("Введите слово: ")
# # Создаем словари с оценками для английского и русского алфавита

# english_scores = {
# 'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,
# 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3,
# 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
# 'Y': 4, 'Z': 10
# }

# russian_scores = {
# 'А': 1, 'Б': 3, 'В': 1, 'Г': 3, 'Д': 2, 'Е': 1, 'Ё': 3, 'Ж': 5,
# 'З': 5, 'И': 1, 'Й': 4, 'К': 2, 'Л': 2, 'М': 2, 'Н': 1, 'О': 1,
# 'П': 2, 'Р': 1, 'С': 1, 'Т': 1, 'У': 2, 'Ф': 10, 'Х': 5, 'Ц': 5,
# 'Ч': 5, 'Ш': 8, 'Щ': 10, 'Ъ': 10, 'Ы': 4, 'Ь': 3, 'Э': 8, 'Ю': 8,
# 'Я': 3
# }

# # Проверяем, что введенное слово содержит только один алфавит

# is_english = all(letter.isalpha() and letter.isupper() for letter in k)
# is_russian = all(letter.isalpha() and letter.isupper() for letter in k)

# if is_english:
# # Вычисляем стоимость английского слова
#     score = sum(english_scores.get(letter, 0) for letter in k)
#     print("Стоимость слова:", score)
# elif is_russian:
# # Вычисляем стоимость русского слова
#     score = sum(russian_scores.get(letter, 0) for letter in k)
#     print("Стоимость слова:", score)
# else:
#     print("Введено некорректное слово.")

# # Вариант 2
# def calculate_word_score(word, language):
#     score = 0
#     if language == "english":
#         scores = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1,
#                    'S': 1, 'T': 1, 'R': 1, 'D': 2, 'G': 2, 'B': 3, 'C': 3,
#                      'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
#                        'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10}
#     elif language == "russian":
#         scores = {'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1,
#                    'Р': 1, 'С': 1, 'Т': 1, 'Д': 2, 'К': 2, 'Л': 2,
#                      'М': 2, 'П': 2, 'У': 2, 'Б': 3, 'Г': 3, 'Ё': 3,
#                        'Ь': 3, 'Я': 3, 'Й': 4, 'Ы': 4, 'Ж': 5, 'З': 5,
#                          'Х': 5, 'Ц': 5, 'Ч': 5, 'Ш': 8, 'Э': 8, 'Ю': 8,
#                            'Ф': 10, 'Щ': 10, 'Ъ': 10}

#     for letter in word.upper():
#         score += scores.get(letter, 0)

#     return score

# word = input("Введите слово: ")
# language = input("Введите язык (english или russian): ")

# word_score = calculate_word_score(word, language)
# print(f"Стоймость слова '{word}' равна {word_score} очков.")


# # Вариант 3
# # Создаем словари с оценками букв для английского и русского алфавитов
# eng_scores = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
#               'D': 2, 'G': 2,
#               'B': 3, 'C': 3, 'M': 3, 'P': 3,
#               'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
#               'K': 5,
#               'J': 8, 'X': 8,
#               'Q': 10, 'Z': 10}
# rus_scores = {'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
#               'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
#               'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
#               'Й': 4, 'Ы': 4,
#               'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
#               'Ш': 8, 'Э': 8, 'Ю': 8,
#               'Ф': 10, 'Щ': 10, 'Ъ': 10}

# # Запрашиваем у пользователя ввод слова
# word = input("Введите слово: ").upper()

# # Проверяем, является ли слово английским или русским
# is_eng = all(letter in eng_scores for letter in word)
# is_rus = all(letter in rus_scores for letter in word)

# # Вычисляем стоимость слова
# score = 0
# if is_eng:
#     score = sum(eng_scores[letter] for letter in word)
# elif is_rus:
#     score = sum(rus_scores[letter] for letter in word)
# else:
#     print("Слово содержит буквы из разных алфавитов")

# # Выводим стоимость слова
# print(f"Стоимость слова {word}:", score)

# # Вариант 4
# # Создаем словари с оценками букв для английского и русского алфавитов
# eng_scores = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
#               'D': 2, 'G': 2,
#               'B': 3, 'C': 3, 'M': 3, 'P': 3,
#               'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
#               'K': 5,
#               'J': 8, 'X': 8,
#               'Q': 10, 'Z': 10}
# rus_scores = {'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
#               'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
#               'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
#               'Й': 4, 'Ы': 4,
#               'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
#               'Ш': 8, 'Э': 8, 'Ю': 8,
#               'Ф': 10, 'Щ': 10, 'Ъ': 10}

# # Запрашиваем у пользователя ввод слова
# word = input("Введите слово: ").upper()

# # Вычисляем стоимость слова
# score = 0
# for letter in word:
#     if letter in eng_scores:
#         score += eng_scores[letter]
#     elif letter in rus_scores:
#         score += rus_scores[letter]

# # Выводим стоимость слова
# print(f"Стоимость слова {word}:", score)

# # Вариант 5
# k = 'ноутбук'
# # 12
# points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
# points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
# word = k.upper()  # переводим все буквы в верхний регистр
# count = 0
# for i in word:
#     if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#         for j in points_en:
#             if i in points_en[j]:
#                 count = count + j
#     else:
#         for j in points_en:
#             if i in points_ru[j]:
#                 count = count + j
# print(count)
