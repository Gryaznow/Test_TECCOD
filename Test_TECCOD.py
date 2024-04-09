#1. Написать функцию, которая принимает на вход список целых чисел и возвращает новый список, содержащий только уникальные элементы из исходного списка.

numbers = [1, 2, 3, 4, 3, 4, 5, 6, 4, 2, 1, 0]

def get_unique_numbers(numbers):
    unique = []

    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique

print(get_unique_numbers(numbers))

#2. Написать функцию, которая принимает на вход два целых числа (минимум и максимум) и возвращает список всех простых чисел в заданном диапазоне.

reslist = []
a = int(input())
b = int(input())
for i in range(a, b + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0 and i != j and j != 1:
            count += 1
    if count == 0:
        reslist.append(i)
print(reslist)

#3. Создать класс Point, который представляет собой точку в двумерном пространстве.
# Класс должен иметь методы для инициализации координат точки, вычисления расстояния до другой точки, а также для получения и изменения координат.

import math

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point):
        distance = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        return distance


p1_x = int(input("p1.x: "))
p1_y = int(input("p1.y: "))

p2_x = int(input("p2.x: "))
p2_y = int(input("p2.y: "))

p1 = Point(p1_x, p1_y)
p2 = Point(p2_x, p2_y)

print(p1.dist(p2))

#4. Написать программу, которая сортирует список строк по длине, сначала по возрастанию, а затем по убыванию.

randomlist = ["aaa", "b", "cc", "dddd", "eee"]
print("Сортировка по возрастанию длины:", sorted(randomlist, key=len))
print("Сортировка по убыванию длины:", sorted(randomlist, key=len, reverse=True))





