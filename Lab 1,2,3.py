#Лабораторная работа №1

#Задача 1:
# num = int(input("Введите число: "))
# for i in range(1, num+1):
#     print(i)

# #Задача 2:
# num1 = int(input('Введите первое число:'))
# num2 = int(input('Ведите второе число:'))
# a = max(num1, num2)
# print('Большое число:', a)
#

#Лабораторная работа №2


# Задача 1:
#
# a = 'Коля'
# def greet(name, msg):
#     print('Привет,', name + '. ' + msg)
# greet(a, 'Доброе утро!')




# a = int(input())
# def square():
#     print(a**2)
# square()



# a = int(input())
# b = int(input())
# def max_of_two(x,y):
#     print(max(x,y))
# max_of_two(a,b)



# #Задание 2:
#
# def describe_person(name, age=30):
#     print(name, age)
# describe_person(input(), input())



# #Задание 3:
#
# a = int(input())
# def is_prime(number):
#     count = 0
#     for i in range(2, int(a**0.5)+1):
#         if a % i == 0:
#             count += 1
#             if a % (a//i) == 0:
#                 count += 1
#     if count == 0:
#         return True
#     if count > 0:
#         return False
# print(is_prime(a))


# Лабораторная работа №3
#
# Задание №1

# def format_text(format):
#     if format == 'целиком':
#         with open(r"D:\инфа\Example\example.txt.txt", 'r', encoding='utf-8') as file:
#             return file.read()
#     elif format == 'построчно':
#         with open(r"D:\инфа\Example\example.txt.txt", 'r', encoding='utf-8') as file:
#             return file.readlines()
#     else:
#         return 'Ошибка ввода'
# print('Какой формат чтения вы хотите выбрать?','\n' + 'чтение целиком или построчно?')
# print(*format_text(input()), sep='')

# Задание №2
#
# def write_text(write):
#     if write == 'написать новый текст':
#         with open(r"D:\инфа\Example\example.txt.txt", 'w', encoding='utf-8') as file:
#             file.write('\n' + input())
#     elif write == 'дописать текст':
#         with open(r"D:\инфа\Example\example.txt.txt", 'a', encoding='utf-8') as file:
#             file.write('\n' + input())
#     else:
#         return 'Ошибка ввода'
#     return file
# print('Вы хотите написать новый текст или дописать текст?')
# print(write_text(input()))

# Задание №3

# def format_text(format):
#     try:
#         if format == 'целиком':
#             with open(r"D:\инфа\Example\example.txt.txt", 'r', encoding='utf-8') as file:
#                 return file.read()
#         elif format == 'построчно':
#             with open(r"D:\инфа\Example\example.txt.txt", 'r', encoding='utf-8') as file:
#                 return file.readlines()
#         else:
#             return 'Ошибка ввода'
#     except:
#         return 'FileNotFoundError'
# print('Какой формат чтения вы хотите выбрать?','\n' + 'чтение целиком или построчно?')
# print(*format_text(input()), sep='')
