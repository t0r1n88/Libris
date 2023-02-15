# 1.4.5
# class MediaPlayer:
#     """
#     Класс для работы с медиа файлами
#     """
#     def open(self,file):
#         """
#         Функция для получения имени файла
#         :param file: путь к файлу
#         """
#         self.filename = file
#
#     def play(self):
#         """
#         Функция для воспроизведения файла
#         """
#         print(f'Воспроизведение {self.filename}')
#
#
# media1 = MediaPlayer()
# media2 = MediaPlayer()
#
# media1.open('filemedia1')
# media2.open('filemedia2')
#
# media1.play()
# media2.play()

# 1.4.6
# class Graph:
#     """
#     Класс для работы с графикой
#     """
#     LIMIT_Y = [0, 10]  # Атрибут класса
#
#     def set_data(self, data):
#         """
#         Функция для получения списка чисел
#         :param data: список чисел
#         """
#         self.data = data
#
#     def draw(self):
#         """
#         Метод для проверки вхождения числа из списка self.data в границы указанные в LIMIT_Y
#         """
#         self.lst_in_data = [] # создаем список
#         for value in self.data:
#             if Graph.LIMIT_Y[0] <= value <= Graph.LIMIT_Y[1]:
#                 self.lst_in_data.append(value)
#
#         print(*self.lst_in_data)
#
#
# graph_1  = Graph()
# graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
# graph_1.draw()

# 1.4.8
#
# import sys
#
#
# class StreamData:
#     """
#     Класс для тренировки
#     """
#
#     def create(self, fields, lst_values):
#         """
#
#         :param fields: кортеж с именами для локальных атрибутов которые нужно создать
#         :param lst_values: список с данными которые нужно рассовать по локальным атрибутам
#         :return: True or False
#         """
#         if len(fields) != len(lst_values):
#             return False
#         else:
#             for idx, local_attr in enumerate(fields):
#                 setattr(self, local_attr, lst_values[idx])
#             return True
#
#
#
#
# class StreamReader:
#     FIELDS = ('id', 'title', 'pages')
#
#     def readlines(self):
#         lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
#         sd = StreamData()
#         res = sd.create(self.FIELDS, lst_in)
#         return sd, res
#
#
# sr = StreamReader()
# data, result = sr.readlines()

# 1.4.10

# class DataBase:
#     """
#     Класс дял хранения введенных строк
#     """
#     lst_data = []
#     FIELDS = ('id', 'name', 'old', 'salary')
#
#     def select(self, a, b):
#         """
#         Возвращает список из словарей по индексам от a до b
#         :param a: начальный индекс
#         :param b: конечный индекс
#         :return: список
#         """
#         return DataBase.lst_data[a:b+1]
#
#     def insert(self, data):
#         """
#         Метод для добавления в словарь данных из списка
#         :param data: список строк
#         """
#         for str_data in data:
#             id_l, name, old, salary = str_data.split(' ')
#             DataBase.lst_data.append({'id': id_l, 'name': name, 'old': old, 'salary': salary})

# 1.4.11

class Translator:
    """
    Класс для перевода с английского на русский
    """
    def add(self,eng,rus):
        """
        Метод для добавления связки английского слова и русского
        :param eng: английское
        :param rus: русское
        """
        if eng not in self.__dict__:
            self.__dict__[eng] = [rus]
        else:
            if rus not in self.__dict__[eng]: # проверяем наличие
                self.__dict__[eng].append(rus)


    def remove(self,eng):
        """
        Метод для удаления из словаря
        :param eng: ключ
        """
        self.__dict__.pop(eng,None)

    def translate(self,eng):
        """
        Метод для вызова по ключу словаря соответствующего содержимого
        :param eng: ключ
        """
        return self.__dict__[eng]


tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")

tr.remove('car')

print(*tr.translate('go'))