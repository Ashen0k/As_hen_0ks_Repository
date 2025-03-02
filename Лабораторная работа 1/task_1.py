import doctest

# TODO Написать 3 класса с документацией и аннотацией типов

class Sword:
    """
    Класс, представляющий информацию о прямом мече.
    Вес и длина клинка указываются в граммах и миллиметрах.

    Примеры:
    >>> broadsword = Sword("сталь", 3500, 950)
    >>> broadsword.material
    'сталь'
    >>> broadsword.weight
    3500
    >>> broadsword.length
    950
    """
    def __init__(self, material: str, weight: int, blade_length: int):
        """
        Создание экземпляра класса Sword.

        Args:
            material: Материал клинка.
            weight: Вес меча в граммах.
            blade_length: Длина клинка в миллиметрах.
        """
        self.material = material
        self.weight = weight
        self.length = blade_length

    def info(self) -> str:
        """
        Вывод всей имеющейся информации о мече.

        Returns:
            Строка с информацией о мече.

        Примеры:
        >>> broadsword = Sword("сталь", 3500, 950)
        >>> broadsword.info()
        'Материал - сталь, вес - 3500 грамм, длина клинка - 950 мм'
        """
        return f"Материал - {self.material}, вес - {self.weight} грамм, длина клинка - {self.length} мм"

class Axe:
    """
    Класс, представляющий информацию о топоре.
    Вес и длина головки указываются в граммах и миллиметрах.

    Примеры:
    >>> light_axe = Axe("сталь", 2500, 350)
    >>> light_axe.material
    'сталь'
    >>> light_axe.weight
    2500
    >>> light_axe.length
    350
    """
    def __init__(self, material: str, weight: int, head_length: int):
        """
        Создание экземпляра класса Axe.

        Args:
            material: Материал топора.
            weight: Вес топора в граммах.
            head_length: Длина головки топора в миллиметрах.
        """
        self.material = material
        self.weight = weight
        self.length = head_length

    def info(self) -> str:
        """
        Вывод всей имеющейся информации о топоре.

        Returns:
            Строка с информацией о топоре.

        Примеры:
        >>> light_axe = Axe("сталь", 2500, 350)
        >>> light_axe.info()
        'Материал - сталь, вес - 2500 грамм, длина головки - 350 мм'
        """
        return f"Материал - {self.material}, вес - {self.weight} грамм, длина головки - {self.length} мм"

class Hammer:
    """
    Класс, представляющий информацию о молоте.
    Вес и площадь бойка указываются в граммах и метрах в квадрате.

    Примеры:
    >>> wood_hammer = Hammer("дерево", 5000, 0.15)
    >>> wood_hammer.material
    'дерево'
    >>> wood_hammer.weight
    5000
    >>> wood_hammer.face
    0.15
    """
    def __init__(self, material: str, weight: int, face_area: float):
        """
        Создание экземпляра класса Hammer.

        Args:
            material: Материал молота.
            weight: Вес молота в граммах.
            face_area: Площадь бойка в квадратных метрах.
        """
        self.material = material
        self.weight = weight
        self.face = face_area

    def info(self) -> str:
        """
        Вывод всей имеющейся информации о молоте.

        Returns:
            Строка с информацией о молоте.

        Примеры:
        >>> wood_hammer = Hammer("дерево", 5000, 0.15)
        >>> wood_hammer.info()
        'Материал - дерево, вес - 5000 грамм, площадь бойка - 0.15 м^2'
        """
        return f"Материал - {self.material}, вес - {self.weight} грамм, площадь бойка - {self.face} м^2"


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()

    pass
