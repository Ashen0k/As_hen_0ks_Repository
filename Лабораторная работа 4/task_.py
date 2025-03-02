if __name__ == "__main__":

class Vehicle:

    def __init__(self, make: str, model: str):

        #Конструктор класса Vehicle
        #Аргументы:
        #    make: марка транспортного средства
        #    model: модель ТС

        self._make = make  # Инкапсулирован для контроля доступа и возможной валидации в будущем
        self._model = model  # Инкапсулирован с той же целью

    def __str__(self) -> str:
        #Возвращает строковое представление объекта Vehicle
        return f"{self.__class__.__name__}: {self._make} {self._model}"

    def __repr__(self) -> str:
        #Возвращает строковое представление объекта Vehicle для отладки
        return f"{self.__class__.__name__}(make={self._make!r}, model={self._model!r})"

    def start_engine(self) -> str:
        #Запускает двигатель ТС
        return "Двигатель запущен."


class Car(Vehicle):

    #Класс для легковых автомобилей, наследуется от Vehicle

    def __init__(self, make: str, model: str, num_doors: int):

        #Конструктор класса Car
        #Аргументы:
        #    make: марка автомобиля
        #    model: модель автомобиля
        #    num_doors: количество дверей

        super().__init__(make, model)
        self._num_doors = num_doors  # Инкапсулирован, чтобы убедиться что это целое число

    def __str__(self) -> str:
        #Возвращает строковое представление объекта Car
        return f"{super().__str__()}, Количество дверей: {self._num_doors}"

    def __repr__(self) -> str:
        #Возвращает строковое представление объекта Car для отладки
        return f"{self.__class__.__name__}(make={self._make!r}, model={self._model!r}, num_doors={self._num_doors})"

    def start_engine(self) -> str:

        #Перегружает метод start_engine базового класса Vehicle
        #Причина: может быть запуск двигателя у легкового автомобиля происходит как-то иначе

        return "Двигатель легкового автомобиля запущен."

    def beep(self) -> str:
        #Издает звук гудка
        return "Би-ип."


class Truck(Vehicle):

    #Класс для грузовых автомобилей, наследуется от Vehicle

    def __init__(self, make: str, model: str, load_capacity: float):

        #Конструктор класса Truck
        #Аргументы:
        #    make: марка грузовика
        #    model: модель грузовика
        #    capacity: грузоподъемность грузовика в тоннах

        super().__init__(make, model)
        self._capacity = capacity  # Инкапсулирован, чтобы гарантировать что грузоподъемность больше нуля

    def __str__(self) -> str:
        #Возвращает строковое представление объекта Truck
        return f"{super().__str__()}, Грузоподъемность: {self._capacity} тонн"

    def __repr__(self) -> str:
        #Возвращает строковое представление объекта Truck для отладки
        return f"{self.__class__.__name__}(make={self._make!r}, model={self._model!r}, capacity={self._capacity})"

    def start_engine(self) -> str:

        #Перегружает метод start_engine базового класса Vehicle
        #Причина: может быть запуск двигателя у грузовоого автомобиля происходит как-то иначе

        return "Двигатель грузовика запущен."

    def load_cargo(self, weight: float) -> str:
        #Загружает груз в грузовик
        #Аргумент:
        #    weight: вес груза в тоннах.
        if weight > self._capacity:
            return "Превышена грузоподъемность!"
        else:
            return "Груз успешно загружен."

    pass