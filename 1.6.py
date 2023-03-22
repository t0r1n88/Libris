"""
изучение магического метода__new__
"""
# 1.6


# class AbstractClass:
#     """
#     класс чтобы тренировки синглтона
#     """
#     __instance = None
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             return 'Ошибка: нельзя создавать объекты абстрактного класса'
#
#
# obj = AbstractClass()

# 1.7

# class SingletonFive:
#     """
#     Класс для отработки создания экземпляров класс в заданном количестве используя паттерн Синглтон
#     """
#     __lst_instance = []
#
#     def __new__(cls, *args, **kwargs):
#         """
#         Переопределяем метод для того чтобы контролировать количество создаваемых объектов
#         :param args:
#         :param kwargs:
#         """
#         if len(cls.__lst_instance) < 5:
#             obj_class = super().__new__(cls)
#             cls.__lst_instance.append(obj_class)
#             return obj_class
#         else:
#             # возвращаем ссылку на пятый объект класса
#             return cls.__lst_instance[-1]
#
#     def __init__(self,name):
#         self.name = name




