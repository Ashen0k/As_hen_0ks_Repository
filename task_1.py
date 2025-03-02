import doctest

# TODO Написать 3 класса с документацией и аннотацией типов

class Sword:
    def __init__(self, material: str, weight: int, blade_length: int):
        """
        Создание информации о прямом мече
        Вес и длина клинка указываются в миллиметрах

        broadsword = Sword("сталь", 3500, 950)
        """
        self.material = material
        self.weight = weight
        self.length = blade_length

    def info(self) -> str:
        """
        Вывод всей имеющейся информации о мече

        broadsword.info()
        'Материал - сталь, вес - 3500 гр, длина клинка - 950 мм'
        """
        return f"Материал - {self.material}, вес - {self.weight} грамм, длина клинка - {self.blade_length} мм"

class Axe:
    def __init__(self, material: str, weight: int, head_length: int):
        """
        Создание информации о топоре
        вес и длина головки указываются в граммах и миллиметрах

        light_axe = Axe("сталь", 2500, 350)
        """
        self.material = material
        self.weight = weight
        self.length = head_length

    def info(self) -> str:
        """
        Вывод всей имеющейся информации о топоре

        light_axe.info()
        'Материал - сталь, вес - 2500 гр, длина головки - 350 мм'
        """
        return f"Материал - {self.material}, вес - {self.weight} грамм, длина головки - {self.head_length} мм"

class Sword:
    def __init__(self, material: str, weight: int, face_area: float):
        """
        Создание информации о молоте
        вес и площадь бойка указываютсяв граммах и метрах в квадрате

        wood_hammer = Hammer("дерево", 5000, 0.15)
        """
        self.material = material
        self.weight = weight
        self.face = face_area

    def info(self) -> str:
        """
        Вывод всей имеющейся информации о мече

        wood_hammer.info()
        'Материал - дерево, вес - 5000 гр, площадь бойка - 0.15 м^2'
        """
        return f"Материал - {self.material}, вес - {self.weight} грамм, площадь бойка - {self.face_area} м^2"


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()

    pass
