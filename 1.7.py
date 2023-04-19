"""
изучения classmethod и  staticmethod
"""
from string import ascii_lowercase, digits


# 1.6
# class Factory:
#     """
#     клвсс с статическими методами для обработки строк
#     """
#     @staticmethod
#     def build_sequence():
#         return []
#
#     @staticmethod
#     def build_number(string):
#         return int(string)
#
# class Loader:
#     @staticmethod
#     def parse_format(string, factory):
#         seq = factory.build_sequence()
#         for sub in string.split(","):
#             item = factory.build_number(sub)
#             seq.append(item)
#
#         return seq
#
# res = Loader.parse_format("4, 5, -6", Factory)
# print(res)


# 1.8
# class CardCheck:
#     """
#     класс для проверки информации на пластиковых картах
#     """
#     CHARS_FOR_NAME = ascii_lowercase.upper() + digits
#
#     @classmethod
#     def check_card_number(cls,number):
#         if len(number.split('-')) != 4:
#             return False
#         for part in  number.split('-'):
#             if not part.isdigit() or len(part) != 4:
#                 return False
#         return True
#
#     @classmethod
#     def check_name(cls,name):
#         if len(name.split(' ')) !=2:
#             return False
#         for part in name.split(' '):
#             for symbols in part:
#                 if symbols not in cls.CHARS_FOR_NAME:
#                     return False
#         return True


# 1.9
# class Video:
#     """
#     класс для эмуляции работы с видео
#     """
#
#     def create(self, name):
#         self.name = name
#
#     def play(self):
#         print(f'воспроизведение видео {self.name}')
#
# class YouTube:
#     """
#     класс для имитации плейлиста ютуб
#     """
#     videos = []
#
#     @classmethod
#     def add_video(cls,video):
#         cls.videos.append(video)
#
#
#     @classmethod
#     def play(cls,video_indx):
#         cls.videos[video_indx].play()
#
#
# v1 = Video()
# v2 = Video()
# v1.create('Python')
# v2.create('Python ООП')
# YouTube.add_video(v1)
# YouTube.add_video(v2)
# YouTube.play(0)
# YouTube.play(1)


# 1.10
#
# class AppStore:
#     """
#     класс для имитации магазина приложений
#     """
#     __lst_app = [] # атрибут класс для хранения экзмепляров классов приложений
#
#
#
#     def add_application(self, app):
#         self.__lst_app.append(app)
#
#     def remove_application(self, app):
#         self.__lst_app.remove(app)
#
#     def block_application(self, app):
#         app.blocked = True
#
#     def total_apps(self):
#         return len(self.__lst_app)
#
# class Application:
#     """
#     класс для описания приложения
#     """
#     def __init__(self, name):
#         self.name = name
#         self.blocked = False
#
#
# store = AppStore()
# app_youtube = Application("Youtube")
# store.add_application(app_youtube)
# store.remove_application(app_youtube)
# store.block_application(app_youtube)

# 1.7

class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


class TextInput:
    """
    клаас для ввода размера поля
    """
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits
    def __init__(self,name, size=10):
        self.name = name # сохраняет название для поля
        self.size = size # размер поля ввода

    def get_html(self):
        return f"<p class='login'><{self.name}>: <input type='text' size=<{self.size}> />"

    @classmethod
    def check_name(cls,name):
        if 3 <= len(name) <= 50 and set(name) in cls.CHARS_CORRECT:


class PasswordInput:
    """
    клаас для ввода размера пароля
    """
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits
    def __init__(self,name, size=10):
        self.name = name # сохраняет название для поля
        self.size = size # размер поля ввода

    def get_html(self):
        return f"<p class='password'><{self.name}>: <input type='text' size=<{self.size}> />"


