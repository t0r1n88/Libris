"""
Инициализатор и финализатор экземпляра класса __init__  __del__
"""


# 1.5.4

# class Point:
#     """
#     класс для создания точек на плоскости
#     """
#
#     def __init__(self, x, y, color='black'):
#         self.x = x
#         self.y = y
#         self.color = color
#
#
# points = [Point(i, i) if i != 3 else Point(i, i, 'yellow') for i in range(1, 2000, 2)]

# 1.5.5
# import random
#
#
# class Line:
#     """
#     Класс для линии
#     """
#
#     def __init__(self, a, b, c, d):
#         self.sp = a, b
#         self.ep = c, d
#
#
# class Rect:
#     """
#     Класс для прямоугольника
#     """
#
#     def __init__(self, a, b, c, d):
#         self.sp = a, b
#         self.ep = c, d
#
#
# class Ellipse:
#     """
#     Класс для овала
#     """
#
#     def __init__(self, a, b, c, d):
#         self.sp = a, b
#         self.ep = c, d
#
#
# elements = []
# for i in range(217):
#     a, b, c, d = random.randint(0, 1000), random.randint(0, 1000), random.randint(0, 1000), random.randint(0, 1000)
#     # Создаем случайный класс
#     foo = random.choice((Line, Rect, Ellipse))
#     elements.append(foo(a, b, c, d))
#
# for value in elements:
#     if isinstance(value, Line):
#         value.sp = (0, 0)
#         value.ep = (0, 0)

# 1.5.6

class TriangleChecker:
    """
    Класс для треугольника
    """

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not all(map(lambda x: type(x) in (int, float), (self.a, self.b, self.c))):
            return 1
        elif any(map(lambda x: x <= 0, (self.a, self.b, self.c))):
            return 1
        elif self.a >= self.b + self.c or self.b >=self.a + self.c or self.c >= self.a + self.b:
            return 2
        else:
            return 3



a, b, c = map(int, input().split())

tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
