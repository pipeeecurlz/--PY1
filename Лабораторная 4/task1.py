import doctest


class FootballPlayers:
    """
    Базовый класс "Футбольные игроки".
    :param name: Имя игрока
    :param country: Гражданство игрока
    :param goals: Количество голов
    :param assists: Количество голевых передач
    :param trophies: Количество трофеев
    Примеры:
    >>> player = FootballPlayers('Тони Кроос', 'Германия', 5, 15, 26)  # инициализация экземпляра класса
    """
    def __init__(self, name: str, country: str, goals: int, assists: int, trophies: int):
        if not isinstance(name, str):
            raise TypeError('Имя игрока должно быть типа str.')

        if not isinstance(country, str):
            raise TypeError('Гражданство игрока должно быть типа str.')

        if not isinstance(goals, int):
            raise TypeError('Количество голов должно быть типа int.')
        if goals < 0:
            raise ValueError('Количество голов не может быть меньше 0')

        if not isinstance(assists, int):
            raise TypeError('Количество голевых передач должно быть типа int.')
        if assists < 0:
            raise ValueError('Количество голевых передач не может быть меньше 0')

        self.name = name
        self.country = country
        self.goals = goals
        self.assists = assists
        self.trophies = trophies

    def __str__(self):
        return f'''
        Игрок: {self.name}. 
        Гражданство: {self.country}. 
        Голы: {self.goals}. 
        Голевые передачи: {self.assists}. 
        Трофеи: {self.trophies}.
        '''

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.country!r}, goals={self.goals}, assists={self.assists}, trophies={self.trophies})"

    def is_top_player(self) -> bool:
        """
        Функция, которая вычисляет, является ли игрок игроком топ-уровня.
        :return: Является ли игрок игроком топ-уровня
        Примеры:
        >>> player = FootballPlayers('Тони Кроос', 'Германия', 5, 15, 26)
        >>> player.is_top_player()
        True
        """
        if self.trophies > 10:
            return True
        else:
            return False

    def is_top_striker(self) -> bool:
        """
        Функция, которая вычисляет, является ли игрок нападающим топ-уровня.
        :return: Является ли игрок нападающим топ-уровня
        Примеры:
        >>> player = FootballPlayers('Эрлинг Холанд"', 'Норвегия', 36, 2, 1)
        >>> player.is_top_striker()
        True
        """
        if self.goals > 30:
            return True
        else:
            return False

    def is_top_playmaker(self) -> bool:
        """
        Функция, которая вычисляет, является ли игрок плеймейкером топ-уровня.
        :return: Является ли игрок плеймейкером топ-уровня
        Примеры:
        >>> player = FootballPlayers('Педри', 'Испания', 10, 15, 1)
        >>> player.is_top_playmaker()
        True
        """
        if self.goals >= 10 and self.assists >= 10:
            return True
        else:
            return False


class Forwards(FootballPlayers):
    """
    Дочерний класс "Нападающие".
    :param name: Имя игрока
    :param country: Гражданство игрока
    :param goals: Количество голов
    :param assists: Количество голевых передач
    :param trophies: Количество трофеев
    :param xG: Показатель xG (ожидаемые голы)
    Примеры:
    >>> player = Forwards('Эрлинг Холанд"', 'Норвегия', 36, 2, 1, 36.41)  # инициализация экземпляра класса
    """
    def __init__(self, name: str, country: str, goals: int, assists: int, trophies: int, xG: float):
        super().__init__(name=name, country=country, goals=goals, assists=assists, trophies=trophies)

        if not isinstance(xG, float):
            raise TypeError('Показатель xG должен быть типа float.')

        self.xG = xG

    def __str__(self):
        return f'''
        Игрок: {self.name}. 
        Гражданство: {self.country}. 
        Голы: {self.goals}. 
        Трофеи: {self.trophies}. 
        xG: {self.xG}
        '''

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.country!r}, goals={self.goals}, trophies={self.trophies}, xG={self.xG})"

    def is_top_player(self) -> bool:
        """
        Функция, которая вычисляет, является ли нападающий игроком топ-уровня.
        :return: Является ли нападающий игроком топ-уровня
        Примеры:
        >>> player = Forwards('Эрлинг Холанд"', 'Норвегия', 36, 2, 1, 36.41)
        >>> player.is_top_player()
        False
        """
        return super().is_top_player()

    def is_top_striker(self) -> bool:
        """
        Функция, которая вычисляет, является ли игрок нападающим топ-уровня.
        :return: Является ли игрок нападающим топ-уровня
        Примеры:
        >>> player = Forwards('Эрлинг Холанд"', 'Норвегия', 36, 2, 1, 36.41)
        >>> player.is_top_striker()
        True
        """
        if self.goals > 30 or self.goals <= int(self.xG):  # перегрузка метода с учетом нового атрибута xG
            return True
        else:
            return False


class Midfielders(FootballPlayers):
    """
    Дочерний класс "Полузащитники".
    :param name: Имя игрока
    :param country: Гражданство игрока
    :param goals: Количество голов
    :param assists: Количество голевых передач
    :param trophies: Количество трофеев
    :param xA: Показатель xA (ожидаемые голевые передачи)
    Примеры:
    >>> player = Midfielders('Педри', 'Испания', 10, 15, 1, 14.26)  #инициализация экземпляра класса
    """
    def __init__(self, name: str, country: str, goals: int, assists: int, trophies: int, xA: float):
        super().__init__(name=name, country=country, goals=goals, assists=assists, trophies=trophies)

        if not isinstance(xA, float):
            raise TypeError('Показатель xA должен быть типа float.')

        self.xA = xA

    def __str__(self):
        return f'''
        Игрок: {self.name}.
        Гражданство: {self.country}. 
        Голы: {self.goals}. 
        Голевые передачи: {self.assists}. 
        Трофеи: {self.trophies}. 
        xA: {self.xA}
        '''

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.country!r}, goals={self.goals}, assists={self.assists}, trophies={self.trophies}, xA={self.xA})"

    def is_top_player(self) -> bool:
        """
        Функция, которая вычисляет, является ли полузащитник игроком топ-уровня.
        :return: Является ли полузащитник игроком топ-уровня
        Примеры:
        >>> player = FootballPlayers('Тони Кроос', 'Германия', 5, 15, 26)
        >>> player.is_top_player()
        True
        """
        return super().is_top_player()

    def is_top_playmaker(self) -> bool:
        """
        Функция, которая вычисляет, является ли игрок плеймейкером топ-уровня.
        :return: Является ли игрок плеймейкером топ-уровня
        Примеры:
        >>> player = Midfielders('Педри', 'Испания', 10, 15, 1, 14.26)
        >>> player.is_top_playmaker()
        True
        """
        if (self.goals >= 10 and self.assists >= 10) or self.assists <= int(self.xA): # перегрузка метода с учетом нового атрибута xA
            return True
        else:
            return False


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации