import doctest

class Ort_triangle:
    def __init__(self, cathet_1: int, cathet_2: int, hypotenuse: int):
        """
        Создание и подготовка к работе объекта "Прямоугольный треугольник"
        :param cathet_1: Первый катет треугольника
        :param cathet_2: Второй катет треугольника
        :param hypotenuse: Гипотенуза
        Примеры:
        >>> triangle = Ort_triangle(3, 4, 5)  # инициализация экземпляра класса
        """
        if not isinstance(cathet_1, int):
            raise TypeError("Катет 1 должен быть типа int")
        if cathet_1 <= 0:
            raise ValueError("Катет 1 должен быть положительным числом")
        self.cathet_1 = cathet_1

        if not isinstance(cathet_2, int):
            raise TypeError("Катет 2 должен быть типа int")
        if cathet_2 <= 0:
            raise ValueError("Катет 2 должен быть положительным числом")
        self.cathet_2 = cathet_2

        if not isinstance(hypotenuse, int):
            raise TypeError("Гипотенуза должна быть типа int")
        if cathet_1 ** 2 + cathet_2 ** 2 != hypotenuse ** 2:
            raise ValueError("Числа должны удовлетворять теореме Пифагора")
        self.hypotenuse = hypotenuse

    def area(self) -> int:
        """
        Функция, которая вычисляет площадь прямоугольного треугольника
        :return: Площадь треугольника
        Примеры:
        >>> triangle = Ort_triangle(3, 4, 5)
        >>> triangle.area()
        6.0
        """
        return self.cathet_1 * self.cathet_2 / 2

    def perimeter(self):
        """
        Функция, которая вычисляет периметр прямоугольного треугольника
        :return: Периметр треугольника
        Примеры:
        >>> triangle = Ort_triangle(3, 4, 5)
        >>> triangle.perimeter()
        12
        """
        return self.cathet_1 + self.cathet_2 + self.hypotenuse


class Parallelepiped:
    def __init__(self, lenght: int, width: int, height: int):
        """
        Создание и подготовка к работе объекта "Параллелепипед"
        :param lenght: Длина параллелепипеда
        :param width: Ширина параллелепипеда
        :param height: Высота параллелепипеда
        Примеры:
        >>> figure = Parallelepiped(2, 6, 5)  # инициализация экземпляра класса
        """
        if not isinstance(lenght, int):
            raise TypeError("Длина должна быть типа int")
        if lenght <= 0:
            raise ValueError("Длина должна быть положительным числом")
        self.length = lenght

        if not isinstance(width, int):
            raise TypeError("Ширина должна быть типа int")
        if width <= 0:
            raise ValueError("Ширина должна быть положительным числом")
        self.width = width

        if not isinstance(height, int):
            raise TypeError("Высота должна быть типа int")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        self.height = height

    def surface_area(self) -> int:
        """
        Функция, которая вычисляет площадь поверхности параллелепипеда
        :return: Площадь поверхности параллелепипеда
        Примеры:
        >>> figure = Parallelepiped(2, 6, 5)
        >>> figure.surface_area()
        104
        """
        return 2 * (self.length * self.width) + 2 * (self.width * self.height) + 2 * (self.length * self.height)

    def volume(self):
        """
        Функция, которая вычисляет объём параллелепипеда
        :return: Объём параллелепипеда
        Примеры:
        >>> figure = Parallelepiped(2, 6, 5)
        >>> figure.volume()
        60
        """
        return self.length * self.width * self.height

class FootballTactics:
    def __init__(self, scheme: list, pressure_type: str, game_style: str):
        """
        Создание и подготовка к работе объекта "Футбольные тактики"
        :param scheme: Игровая схема команды
        :param pressure_type: Тип прессинга, используемый командой
        :param height: Игровой стиль команды
        Примеры:
        >>> team_1 = FootballTactics([4, 3, 3], 'высокий блок', 'позиционный футбол')  # инициализация экземпляра класса
        """
        if not isinstance(scheme, list):
            raise TypeError("Схема должна быть типа list")
        if sum(scheme) != 10:
            raise ValueError("В футболе 10 полевых игроков")
        self.scheme = scheme

        if not isinstance(pressure_type, str):
            raise TypeError("Тип прессинга должен быть типа str")
        self.pressure_type = pressure_type

        if not isinstance(game_style, str):
            raise TypeError("Игровой стиль должен быть типа str")
        self.game_style = game_style

    def is_offensive(self):
        """
        Функция, которая проверяет, является ли команда атакующей
        :return: Является ли команда атакующей
        Примеры:
        >>> team_1 = FootballTactics([3, 5, 2], 'высокий блок', 'позиционный футбол')
        >>> team_1.is_offensive()
        True
        """
        gamestyles_list = ['позиционный футбол', 'контрпрессинг']
        if self.scheme[0] <= 4 and self.pressure_type == 'высокий блок' and self.game_style in gamestyles_list:
            return True
        else:
            return False

    def is_defensive(self):
        """
        Функция, которая проверяет, играет ли команда от обороны
        :return: Играет ли команда от обороны
        Примеры:
        >>> team_1 = FootballTactics([5, 4, 1], 'низкий блок', 'контратаки')
        >>> team_1.is_defensive()
        True
        """
        gamestyles_list = ['длинные передачи', 'контратаки']
        if self.scheme[0] > 4 and self.pressure_type == 'низкий блок' and self.game_style in gamestyles_list:
            return True
        else:
            return False

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
