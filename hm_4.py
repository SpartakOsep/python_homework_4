# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# num = int(input("Введите число: "))
# i = 2 
# lst = []
# old = num
# while i <= num:
#     if num % i == 0:
#         lst.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {old} находятся в списке: {lst}")

# 2 - Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Исходный список: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f"Список из неповторяющихся элементов: {new_lst}")

# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# 12A11B10C6D5E4FG python is s7o c7ol
# Первая функция - текст зашифровывает
# Вторая - расшифровывает
# Две промежуточные - считывают с файла и записывают в файл

with open('file_homework_4.txt', 'w') as data:
    data.write("AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool")

with open('file_homework_4.txt', 'r') as data:
    string = data.readline()


