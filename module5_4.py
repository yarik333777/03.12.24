class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        if not args:
            raise ValueError("Необходимо передать хотя бы один аргумент.")
        cls.houses_history.append(args[0])
        instance = super().__new__(cls)
        return instance

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        House.houses_history.append(self.name)
        print(f'This is house {self.name}, number of floors: {self.number_of_floors}')

    def go_to(self, new_floors):
        if new_floors > self.number_of_floors or new_floors < 1:
            print(f"There is no such floor: {new_floors}")
        else:
            print(f'Moving to floor {new_floors}')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Name: {self.name}, quantity floors: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return NotImplemented

    def __iadd__(self, value):
        self.number_of_floors += value
        return self

    def __add__(self, value):
        return self.number_of_floors + value

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return NotImplemented

h11 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h21 = House('ЖК Акация', 20)
print(House.houses_history)
h31 = House('ЖК Матрёшка', 20)
print(House.houses_history)
print(h11)
print(h21)
print(h31)
h1 = House('ЖК Горский', 10)
h2 = House('Домик в деревне', 20)
h1.go_to(5)
h2.go_to(10)
print(len(h1))
print(len(h2))
print(str(h1))
print(str(h2))

print(h1 == h2)  # __eq__

h1 += 10  # __iadd__
print(h1.number_of_floors)
print(h1 == h2)

h2 += 10  # __iadd__
print(h2.number_of_floors)

print(h1 > h2)   # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)   # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__











# Как мы уже знаем метод __new__ вызывается перед тем, как вызовется метод __init__.
# Разберёмся, как происходит передача данных между ними на следующем примере.
#
# Работа __new__:
# 'data' передаётся (упаковывается) в *args, т.к. это позиционный аргумент. Он будет находиться под индексом 0 как единственный элемент кортежа.
# second=25 и third=3.14 передаются (упаковываются) в **kwargs т.к. это именованные аргументы. Они будут находиться под ключами 'second' и 'third' со значением 25 и 3.14 соответственно в словаре.
# Передача данных из __new__ в __init__:
# После того как метод __new__ отработает до конца, произойдут следующие события с параметрами __init__:
# В параметр first распакуется из args единственный аргумент 'data'.
# В параметр second распакуется значение под ключом с тем же названием из словаря kwargs.
# В параметр third распакуется значение под ключом с тем же названием из словаря kwargs.
#
#
# Задача "История строительства":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".
#
# В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.
#
# Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.
# Дополните метод __new__ так, чтобы:
# Название объекта добавлялось в список cls.houses_history.
# Название строения можно взять из args по индексу.
#
# Также переопределите метод __del__(self) в котором будет выводиться строка:
# "<название> снесён, но он останется в истории"
#
# Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также значение атрибута houses_history.
#
# Пример результата выполнения программы:
# Пример выполнения программы:
# h1 = House('ЖК Эльбрус', 10)
# print(House.houses_history)
# h2 = House('ЖК Акация', 20)
# print(House.houses_history)
# h3 = House('ЖК Матрёшки', 20)
# print(House.houses_history)
#
# Удаление объектов
# del h2
# del h3
#
# print(House.houses_history)
#
# Вывод на консоль:
# ['ЖК Эльбрус']
# ['ЖК Эльбрус', 'ЖК Акация']
# ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# ЖК Акация снесён, но он останется в истории
# ЖК Матрёшки снесён, но он останется в истории
# ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# ЖК Эльбрус снесён, но он останется в истории
#
# Примечания:
# Более подробно о работе метода __new__ можно узнать здесь.
# В методе __new__ можно обращаться к атрибутам текущего класса при помощи параметра cls.