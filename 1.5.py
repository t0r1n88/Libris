"""
Инициализатор и финализатор экземпляра класса __init__  __del__
"""

import sys


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

# class TriangleChecker:
#     """
#     Класс для треугольника
#     """
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_triangle(self):
#         if not all(map(lambda x: type(x) in (int, float), (self.a, self.b, self.c))):
#             return 1
#         elif any(map(lambda x: x <= 0, (self.a, self.b, self.c))):
#             return 1
#         elif self.a >= self.b + self.c or self.b >=self.a + self.c or self.c >= self.a + self.b:
#             return 2
#         else:
#             return 3
#
#
#
# a, b, c = map(int, input().split())
#
# tr = TriangleChecker(a, b, c)
# print(tr.is_triangle())

# 1.5.7

# class Graph:
#     """
#     класс для создания графиков
#     """
#
#     def __init__(self, data: list):
#         self.data = data.copy()
#         self.is_show = True
#
#     def set_data(self, data: list):
#         self.data.extend(data)
#
#     def show_table(self):
#         if self.is_show:
#             print(' '.join(map(str,self.data)))
#         else:
#             print('Отображение данных закрыто')
#
#     def show_graph(self):
#         if self.is_show:
#             print(f'Графическое отображение данных:{" ".join(map(str,self.data))}')
#         else:
#             print('Отображение данных закрыто')
#
#     def show_bar(self):
#         if self.is_show:
#             print(f'Столбчатая диаграмма:{" ".join(map(str, self.data))}')
#         else:
#             print('Отображение данных закрыто')
#
#     def set_show(self, fl_show):
#         self.is_show = fl_show
#
#
# data_graph = list(map(int, input().split()))
#
# gr = Graph(data_graph)
#
# gr.show_bar()
# gr.set_show(False)
# gr.show_table()

# 1.5.8

#
# class CPU:
#     """
#     класс для описания процессоров
#     """
#     def __init__(self,name,fr):
#         self.name = name
#         self.fr = fr
#
# class Memory:
#     """
#     Класс для описания памяти
#     """
#     def __init__(self,name,volume):
#         self.name = name
#         self.volume = volume
#
# class MotherBoard:
#     """
#     класс для описания материнской платы
#     """
#     def __init__(self,name,cpu,mem_slots):
#         self.name = name
#         self.cpu = cpu
#         self.total_mem_slots = 4
#         self.mem_slots = mem_slots[:self.total_mem_slots]
#
#     def get_config(self):
#         mb = f'Материнская плата: {self.name}'
#         cpu = f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}'
#         mem_slots = f'Слотов памяти: {self.total_mem_slots}'
#         char_memory = [(obj.name,obj.volume)for obj in self.mem_slots]
#         temp_str = ''
#         for memory in char_memory:
#             temp = f'{memory[0]}-{memory[1]};'
#             temp_str += temp
#         temp_str = temp_str[:-1]
#         memory = f'Память: {temp_str}'
#         return [mb,cpu,mem_slots,memory]
#
#
#
# mb = MotherBoard('MSI',CPU('Intel',3000),[Memory('Corsair',4),Memory('Samsung',16)])
#
# print(mb.get_config())
# 1.5.9

# class Table:
#     """
#     класс для столов
#     """
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class TV:
#     """
#     класс для телевизоров
#     """
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Notebook:
#     """
#     класс для ноутбуков
#     """
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Cup:
#     """
#     класс для чашшек
#     """
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Cart:
#     """Класс для корзины"""
#     def __init__(self):
#         self.goods = []
#
#     def add(self,gd):
#         self.goods.append(gd)
#
#     def remove(self,indx):
#         self.goods.pop(indx)
#
#     def get_list(self):
#         lst_temp = [f'{obj.name}:{obj.price}' for obj in self.goods]
#         return lst_temp
#
#
# cart = Cart()
# cart.add(TV('Samsing',2000))
# cart.add(TV('Dawo',4500))
# cart.add(Table('pop',215))
# cart.add(Cup('cupsg',50))
# print(cart.get_list())

# 1.5.10

# class ListObject:
#     """
#     Класс для примера односвязного списка
#     """
#     def __init__(self,data:str,next_obj=None):
#         self.next_obj = next_obj
#         self.data = data
#
#     def link(self,obj):
#         self.next_obj = obj
#
# lst_in = ['Lindy', 'Booth','Lindsey']
#
# head_obj = ListObject(lst_in[0])
# obj = head_obj
# for value in lst_in[1:]:
#     # присоединяем к элементу
#     new_obj = ListObject(value)
#     obj.link(new_obj)
#     obj = new_obj

# 1.5.11

class Cell:
    """
    Класс для клетки
    """
    def __init__(self,mine,around_mines=0):
        self.around_mines = around_mines # число мин вокруг данной клетки поля
        self.mine = mine # наличие мины в текущей клетке
        self.fl_open = False


class GamePole:
    """
    Для управления игровым полем, размером NxN клеток
    """
    def __init__(self,n,m):
        self.n = n # количество клеток
        self.m = m # число мин на поле
        self.pole = []
