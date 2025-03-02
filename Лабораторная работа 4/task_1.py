if __name__ == "__main__":

    class Vehicle:
        """
        Базовый класс для транспортных средств

        Атрибуты:
            make (str): Марка тс
            model (str): Модель тс
        """
        def __init__(self, make: str, model: str):
            """
            Конструктор класса Vehicle

            Args:
                make (str): Марка тс
                model (str): Модель тс
            """
            self._make = make  # Инкапсулирован для контроля доступа и возможной валидации в будущем
            self._model = model  # Инкапсулирован с той же целью

        def __str__(self) -> str:
            """
            Возвращает строковое представление объекта Vehicle

            Returns:
                str: Строковое представление в формате "<Название класса>: <Марка> <Модель>"
            """
            return f"{self.__class__.__name__}: {self._make} {self._model}"

        def __repr__(self) -> str:
            """
            Возвращает строковое представление объекта Vehicle для отладки

            Returns:
                str: Строковое представление, которое можно использовать для создания нового объекта
            """
            return f"{self.__class__.__name__}(make={self._make!r}, model={self._model!r})"

        def start_engine(self) -> str:
            """
            Запускает двигатель тс

            Returns:
                str: Сообщение о запуске двигателя
            """
            return "Двигатель запущен."


    class Car(Vehicle):
        """
        Класс для легковых автомобилей, наследуется от Vehicle

        Атрибуты:
            num_doors (int): Количество дверей
        """
        def __init__(self, make: str, model: str, num_doors: int):
            """
            Конструктор класса Car

            Args:
                make (str): Марка автомобиля
                model (str): Модель автомобиля
                num_doors (int): Количество дверей
            """
            super().__init__(make, model)
            self._num_doors = num_doors  # Инкапсулирован, чтобы убедиться что это целое число

        def __str__(self) -> str:
            """
            Возвращает строковое представление объекта Car

            Returns:
                str: Строковое представление, включающее марку, модель и количество дверей
            """
            return f"{super().__str__()}, Количество дверей: {self._num_doors}"

        def __repr__(self) -> str:
            """
            Возвращает строковое представление объекта Car для отладки

            Returns:
                str: Строковое представление, которое можно использовать для создания нового объекта
            """
            return f"{self.__class__.__name__}(make={self._make!r}, model={self._model!r}, num_doors={self._num_doors})"

        def start_engine(self) -> str:
            """
            Перегружает метод start_engine базового класса Vehicle

            Причина: Запуск двигателя у легкового автомобиля может отличаться

            Returns:
                str: Сообщение о запуске двигателя легкового автомобиля
            """
            return "Двигатель легкового автомобиля запущен."

        def beep(self) -> str:
            """
            Издает звук гудка

            Returns:
                str: Звук гудка
            """
            return "Би-ип."


    class Truck(Vehicle):
        """
        Класс для грузовых автомобилей, наследуется от Vehicle

        Атрибуты:
            _capacity (float): Грузоподъемность грузовика в тоннах
        """
        def __init__(self, make: str, model: str, capacity: float):
            """
            Конструктор класса Truck.

            Args:
                make (str): Марка грузовика
                model (str): Модель грузовика
                capacity (float): Грузоподъемность грузовика в тоннах
            """
            super().__init__(make, model)
            self._capacity = capacity  # Инкапсулирован, чтобы гарантировать что грузоподъемность больше нуля

        def __str__(self) -> str:
            """
            Возвращает строковое представление объекта Truck

            Returns:
                str: Строковое представление, включающее марку, модель и грузоподъемность
            """
            return f"{super().__str__()}, Грузоподъемность: {self._capacity} тонн"

        def __repr__(self) -> str:
            """
            Возвращает строковое представление объекта Truck для отладки

            Returns:
                str: Строковое представление, которое можно использовать для создания нового объекта
            """
            return f"{self.__class__.__name__}(make={self._make!r}, model={self._model!r}, capacity={self._capacity})"

        def start_engine(self) -> str:
            """
            Перегружает метод start_engine базового класса Vehicle.

            Причина: Запуск двигателя у грузового автомобиля может отличаться

            Returns:
                str: Сообщение о запуске двигателя грузовика
            """
            return "Двигатель грузовика запущен."

        def load_cargo(self, weight: float) -> str:
            """
            Загружает груз в грузовик

            Args:
                weight (float): Вес груза в тоннах

            Returns:
                str: Сообщение об успешной загрузке или превышении грузоподъемности
            """
            if weight > self._capacity:
                return "Превышена грузоподъемность!"
            else:
                return "Груз успешно загружен."