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


# 1.6.9
# TYPE_OS = 1
#
# class DialogWindows:
#     name_class = "DialogWindows"
#
#
# class DialogLinux:
#     name_class = "DialogLinux"
#
#
# class Dialog:
#     """
#     класс для создания классов в зависимости от значения константы
#     """
#     def __new__(cls, *args, **kwargs):
#         if TYPE_OS == 1:
#             d_w = DialogWindows()
#             setattr(d_w,'name',*args)
#             return d_w
#         else:
#             d_l = DialogLinux()
#             setattr(d_l, 'name', *args)
#             return d_l
#
# dlg = Dialog('Lindy')

# 1.6.10

# class Point:
#     """
#     Класс для создания точки
#     """
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def clone(self):
#         new_obj = Point(self.x,self.y)
#         return new_obj
#
#
# pt =Point(1,2)
# pt_clone = pt.clone()

#1.6.11

class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq

class Factory:
    """
    класс
    """

    def build_sequence(self):
        return []

    def build_number(self, string):
        """
        для преобразования переданной в метод строки (string) в вещественное значение (метод должен возвращать полученное вещественное число
        """
        return float(string)



ld = Loader()
res = ld.parse_format("4, 5, -6.5", Factory())

print(res)