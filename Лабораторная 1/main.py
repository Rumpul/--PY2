# TODO Написать 3 класса с документацией и аннотацией типов

import doctest


class Application:
    def __init__(self, name: str, memory_needs: int, development_name: str):
        """
        Создание и подготовка к работе объекта Приложение

        :param name: название приложения
        :param memory_needs: количество занимаемой памяти
        :param development_name: название разработчика

        Пример:
        >>> application = Application("Гонки", 12, "Разработчик") # создание экземпляра класса

        """
        if not isinstance(name, str):
            raise TypeError(f"Название приложения должно быть типа str, а не {type(name)}")
        self.name = name
        if not isinstance(memory_needs, int):
            raise TypeError(f"Количество занимаемой памяти должно быть типа int, а не {type(memory_needs)}")
        if memory_needs <= 0:
            raise ValueError("Количество занимаемой памяти не может быть меньше или равно 0")
        self.memory_needs = memory_needs
        if not isinstance(development_name, str):
            raise TypeError(f"Название разработчика должно быть типа str, а не {type(development_name)}")
        self.development_name = development_name

    def turn_on_application(self) -> bool:
        """
        Метод, который позволяет запустить приложение

        :return: возвращает статус приложение (запущено/не удалось запустить)

        Пример:
         >>> application = Application("Гонки", 12, "Разработчик") # создание экземпляра класса Application
         >>> application.turn_on_application() # вызов метода
        """
        ...

    def turn_off_application(self) -> bool:
        """
        Метод, который позволяет закрыть приложение

        :return: возвращает статус приложение (закрыто/не удалось закрыть/приложение не запущено)

        Пример:
         >>> application = Application("Гонки", 12, "Разработчик")
         >>> application.turn_off_application()
        """
        ...


class Phone:
    def __init__(self, model: str, memory_storage: int, price: int, manufacturer_company: str):
        """
        Создание и подготовка к работе объекта Телефон

        :param model: модель телефона
        :param memory_storage: количество памяти в телефоне
        :param manufacturer_company: компания производитель
        :param price: цена телефона

        Пример:
        >>> phone = Phone("Galaxy", 128, 12000, "Samsung" )
        """

        if not isinstance(model, str):
            raise TypeError(f"Модель должна быть типа str, а не {type(model)}")
        self.model = model
        if not isinstance(memory_storage, int):
            raise TypeError(f"Количество памяти должно быть типа int, а не {type(model)}")
        if memory_storage <= 0:
            raise ValueError("Количество памяти не может быть меньше или равно 0")
        self.memory_storage = memory_storage
        if not isinstance(price, int):
            raise TypeError(f"Цена должна быть типа int, а не {type(model)}")
        if price < 0:
            raise ValueError("Цена не может быть меньше  0")
        self.price = price
        if not isinstance(manufacturer_company, str):
            raise TypeError(f"Компания производитель должна быть типа str, а не {type(manufacturer_company)}")
        self.manufacturer_company = manufacturer_company

    def install_application(self, new_application: Application) -> bool:

        """
        Метод установки приложения на телефон

        :param new_application: экземпляр класса Application

        :raise ValueError: Если количество памяти необходимое для установки приложения больше
         количества оставшейся памяти в телефоне, то приложение не установится

        :return: возвращает сообщение об успешной/не успешной установке приложения
        и количество оставшейся памяти

        Пример:
        >>> application = Application("Гонки", 12, "Разработчик")
        >>> phone = Phone("Galaxy", 128, 12000, "Samsung" ) # создание экземпляра класса Phone
        >>> phone.install_application(application) # вызов метода
        """

        if not isinstance(new_application, Application):
            raise TypeError(f"Приложение должно быть типа Application, а не {type(new_application)}")
        if self.memory_storage - new_application.memory_needs < 0:
            raise ValueError("Недостаточно памяти")

        ...

    def clean_all_memory(self) -> None:
        """
        Метод, который позволяет полностью очистить память телефона

        :return: возвращает изначальное количество памяти в экземпляре

        Пример:
        >>> phone = Phone("Galaxy", 128, 12000, "Samsung" )
        >>> phone.clean_all_memory()
        """
        ...


class Shop:
    def __init__(self, name: str, city: str, phones: dict):
        """
        Создание и подготовка к работе объекта Магазин

        :param name: название магазина
        :param city: расположение магазина
        :param phones: список телефонов в магазине


        Пример:
        >>> shop = Shop("Магазин", "Санкт-Петербург", {}) # создание экземпляра класса Shop
        """

        if not isinstance(name, str):
            raise TypeError(f"Название магазина должно быть типа str, а не {type(name)}")
        self.name = name
        if not isinstance(city, str):
            raise TypeError(f"Расположение магазина должно быть типа str, а не {type(city)}")
        self.city = city
        if not isinstance(phones, dict):
            raise TypeError(f"Cписок телефонов должен быть типа Phone, а не {type(phones)}")
        self.phones = phones

    def add_new_phone(self, new_phone: Phone) -> None:
        """
        Метод для добавления телефона

        :param new_phone: телефон, который добавляем

        :raise TypeError: Если телефон не является типом Phone, то вызываем ошибку

        :return: добавляем новый телефон в магазин или увеличиваем количество

        Пример:
        >>> phone = Phone("Galaxy", 128, 12000, "Samsung" )
        >>> shop = Shop("Магазин", "Санкт-Петербург", {}) # создание экземпляра класса Shop
        >>> shop.add_new_phone(phone)
        """
        ...

        if not isinstance(new_phone, Phone):
            raise TypeError(f"Телефон должен быть типа Phone, а не {type(new_phone)}")
        ...

    def get_phone(self, phone_model: str) -> None:
        """
        Метод для продажи телефона

        :param phone_model: телефон, который продаем

        :raise ValueError: Если телефона нет в словаре phones, то выводим ошибку

        :return: убираем телефон из магазина или уменьшаем количество

        Пример:
        >>> shop = Shop("Магазин", "Санкт-Петербург", {}) # создание экземпляра класса Shop
        >>> shop.get_phone("Iphone")
        """

        if not isinstance(phone_model, str):
            raise TypeError(f"Телефон должен быть типа str, а не {type(phone_model)}")
        ...

    def phones_in_shop(self) -> int:
        """
        Метод для подсчета общего количества телефонов в магазине

        :return: количество телефонов в магазине

        Пример:
        >>> shop = Shop("Магазин", "Санкт-Петербург", {}) # создание экземпляра класса Shop
        >>> shop.phones_in_shop()

        """

        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
