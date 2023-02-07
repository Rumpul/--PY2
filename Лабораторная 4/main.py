import doctest


class Device:
    def __init__(self, model: str, year_of_production: int):
        """
        Создание объекта устройства
        :param model: Название модели устройства
        :param year_of_production: Год выпуска устройства
        """
        if not isinstance(model, str):
            raise ValueError("Название модели должно быть строкового типа!")
        self._model = model
        if year_of_production <= 0:
            raise ValueError("Год выпуска должен быть больше 0")
        if not isinstance(year_of_production, int):
            raise TypeError(f"Год выпуска должен быть типа int")
        self._year_of_production = year_of_production
        self._device_enable_status = False  # Статус устройства, при инициализации класса всегда выключено (False)
        self._device_users = []  # Создание пустого словаря пользователей для каждого экземпляра класса

    @property
    def model(self):
        return self._model

    @property
    def year_of_production(self):
        return self._year_of_production

    def __str__(self):
        return f"Модель - {self.model}. Год выпуска - {self.year_of_production}"

    def __repr__(self):
        return f"{self.__class__.__name__}(model={self.model!r}, year_of_production={self.year_of_production!r})"

    def change_device_enable_status(self) -> str:
        """
        Метод, который позволяет включить/выключить устройство
        :return: возвращает статус устройства
        Пример:
         >>> device1 = Device(model="Model", year_of_production=1993)
         >>> device1.change_device_enable_status()
         'Устройство успешно включено'
         >>> device1.change_device_enable_status()
         'Устройство успешно выключено'
        """
        if not self._device_enable_status:
            self._device_enable_status = True
            return 'Устройство успешно включено'
        else:
            self._device_enable_status = False
            return 'Устройство успешно выключено'

    def change_password(self, user_password: str | int):
        """
        Метод для смены пароля пользователя
        :param user_password: Пароль
        :return: Обновляет пароль в списке пользователей
        """
        current_password = input('Для смены пароля введите текущий пароль:')
        for password in range(len(self._device_users)):
            if self._device_users[password]['user_password'] == current_password:
                self._device_users[password]['user_password'] = user_password

    def create_user(self, user_name: str, user_password: str | int):
        """
        Метод, который позволяет создать пользователя устройства
        :param user_name: Имя пользователя
        :param user_password: Пароль
        :return: Метод добавляет пользователя
         >>> device1 = Device(model="Model", year_of_production=1993)
         >>> device1.change_device_enable_status()
         'Устройство успешно включено'
         >>> device1.create_user('user_name','user_password')
         >>> device1.change_device_enable_status()
         'Устройство успешно выключено'
         >>> device1.create_user('user_name','user_password')
         Ваше устройство выключено. Для добавления пользователя его нужно включить
        """
        if self._device_enable_status:
            if not isinstance(user_name, str):
                raise ValueError("Имя пользователя должно быть строкового типа!")
            if not isinstance(user_password, (str, int)):
                raise ValueError("Пароль должен быть str или int!")
            if not self._device_users:
                self._device_users.append({'user_name': user_name, 'user_password': user_password})
            else:
                for i in range(len(self._device_users)):
                    if not self._device_users[i]['user_name'] == user_name:
                        self._device_users.append({'user_name': user_name, 'user_password': user_password})
                    else:
                        raise UserWarning('Для данного пользователя уже существует пароль. '
                                          'Для смены пароля воспользуйтесь другим методом.')
        else:
            print('Ваше устройство выключено. Для добавления пользователя его нужно включить')


class SmartPhone(Device):
    def __init__(self, model: str, year_of_production: int, money_on_sim_card: int | float, user_number: str | int):
        """
        Создание объекта телефон
        :param model: Название модели телефона
        :param year_of_production: Год выпуска телефона
        :param money_on_sim_card: Количество денег на сим карте
        :param user_number: Номер телефона пользователя
        """
        super().__init__(model, year_of_production)
        self._money_on_sim_card = money_on_sim_card
        if not len(str(user_number)) == 11:
            raise ValueError("Номер РФ должен быть длинной в 11 символов")
        if not str(user_number).startswith('7'):
            raise ValueError("Номер РФ должен начинаться с 7")
        if not isinstance(user_number, (str, int)):
            raise TypeError(f"Значение денег на сим карте должно быть типа str или int")
        self._user_number = user_number

    @property
    def money_on_sim_card(self):
        return self._money_on_sim_card

    @money_on_sim_card.setter
    def money_on_sim_card(self, new_money):
        if new_money < 0:
            raise ValueError("Значение денег на сим карте должно быть не меньше 0")
        if not isinstance(new_money, (int, float)):
            raise TypeError(f"Значение денег на сим карте должно быть типа float или int")
        self._money_on_sim_card = new_money

    @property
    def user_number(self):
        return self._user_number

    def __str__(self):
        return f"{super().__str__()}, Количество денег на балансе - {self.money_on_sim_card}, " \
               f"Номер телефона - {self.user_number}"

    def __repr__(self):
        return f"{self.__class__.__name__}(model={self.model!r}, year_of_production={self.year_of_production!r}, " \
               f"money_on_sim_card={self.money_on_sim_card!r}, user_number={self.user_number!r})"

    def call(self, cost_of_call: int | float):
        """
        Метод для совершения звонков по телефону
        :param cost_of_call: Стоимость звонка
        :return: Возвращает сообщение об успешном или не успешном звонке
        >>> smartphone1= SmartPhone(model="Model",year_of_production=1993,money_on_sim_card=53,user_number=71235321234)
        >>> smartphone1.call(10)
        'Звонок состоялся. Остаток на балансе: 43'
        """
        if not isinstance(cost_of_call, (int, float)):
            raise TypeError(f"Значение стоимости звонка должно быть типа float или int")
        if self.money_on_sim_card < cost_of_call:
            return 'Недостаточно денег на балансе'
        else:
            self.money_on_sim_card -= cost_of_call
            return f'Звонок состоялся. Остаток на балансе: {self.money_on_sim_card}'

    def create_user(self, user_name: str, user_password: str | int):
        """
        Перегрузка метода, так как у наследника своя система регистрации пользователя
        :param user_name: Имя пользователя
        :param user_password: Пароль
        :return: Метод добавляет пользователя
         >>> smartphone1 = SmartPhone(model="Model",year_of_production=1993,money_on_sim_card=53,user_number=71235321234)
         >>> smartphone1.change_device_enable_status()
         'Устройство успешно включено'
         >>> smartphone1.create_user('user_name','user_password')
         >>> smartphone1.change_device_enable_status()
         'Устройство успешно выключено'
         >>> smartphone1.create_user('user_name','user_password')
         Ваше устройство выключено. Для добавления пользователя его нужно включить
        """
        if self._device_enable_status:
            if not isinstance(user_name, str):
                raise ValueError("Имя пользователя должно быть строкового типа!")
            if not isinstance(user_password, (str, int)):
                raise ValueError("Пароль должен быть str или int!")
            if not self._device_users:
                self._device_users.append({'user_name': user_name, 'user_password': user_password,
                                           'user_phone': self.user_number})
            else:
                for i in range(len(self._device_users)):
                    if not self._device_users[i]['user_name'] == user_name:
                        raise UserWarning('Нельзя зарегистрировать несколько пользователей телефона. '
                                          'Пользователь может быть только один.')
                    else:
                        raise UserWarning('Для данного пользователя уже существует пароль. '
                                          'Для смены пароля воспользуйтесь другим методом.')
        else:
            print('Ваше устройство выключено. Для добавления пользователя его нужно включить')


class Computer(Device):
    def __init__(self, model: str, year_of_production: int, memory: int):
        """
        Создание объекта компьютер
        :param model: Название модели компьютера
        :param year_of_production: Год выпуска компьютера
        :param memory: Количество памяти компьютера
        """
        super().__init__(model, year_of_production)
        self._memory = memory

    @property
    def memory(self):
        return self._memory

    @memory.setter
    def memory(self, new_memory):
        if new_memory <= 0:
            raise ValueError("Количество памяти компьютера должно быть больше 0")
        if not isinstance(new_memory, int):
            raise TypeError(f"Количество памяти компьютера должно быть типа int")
        self._memory = new_memory

    def __str__(self):
        return f"{super().__str__()}, Количество памяти в компьютере - {self.memory}"

    def __repr__(self):
        return f"{self.__class__.__name__}(model={self.model!r}, year_of_production={self.year_of_production!r}, " \
               f"memory={self.memory!r})"

    def download_application(self, application_need_memory: int):
        """
        Метод для установки приложения на компьютер
        :param application_need_memory: Количество памяти для приложения
        :return: Возвращает сообщение об успешном или не успешном звонке
        >>> computer1= Computer(model="Model",year_of_production=1993,memory=53)
        >>> computer1.download_application(10)
        'Установка прошла успешно. Остаток памяти: 43'
        """
        if not isinstance(application_need_memory, int):
            raise TypeError(f"Количество памяти для приложения должно быть типа int")
        if self.memory < application_need_memory:
            return 'Недостаточно памяти на компьютере'
        else:
            self.memory -= application_need_memory
            return f'Установка прошла успешно. Остаток памяти: {self.memory}'

    def create_user(self, user_name: str, user_password: str | int):
        """
        Перегрузка метода, так как у наследника своя система регистрации пользователя
        :param user_name: Имя пользователя
        :param user_password: Пароль
        :return: Метод добавляет пользователя
         # >>> computer1= Computer(model="Model", year_of_production=1993, memory=53)
         # >>> computer1.change_device_enable_status()
         # 'Устройство успешно включено'
         # >>> computer1.create_user('user_name','user_password')
         # >>> computer1.change_device_enable_status()
         # 'Устройство успешно выключено'
         # >>> computer1.create_user('user_name','user_password')
         # Ваше устройство выключено. Для добавления пользователя его нужно включить
        """
        if self._device_enable_status:
            if not isinstance(user_name, str):
                raise ValueError("Имя пользователя должно быть строкового типа!")
            if not isinstance(user_password, (str, int)):
                raise ValueError("Пароль должен быть str или int!")
            admin_status = input('Является ли пользователь администратором? (Yes/No)\n')
            if not self._device_users:
                self._device_users.append({'user_name': user_name, 'user_password': user_password,
                                           'admin_status': admin_status})
            else:
                for i in range(len(self._device_users)):
                    if not self._device_users[i]['user_name'] == user_name:
                        if not self._device_users[i]['user_name'] == user_name:
                            self._device_users.append({'user_name': user_name, 'user_password': user_password,
                                                       'admin_status': admin_status})
                        else:
                            raise UserWarning('Для данного пользователя уже существует пароль. '
                                              'Для смены пароля воспользуйтесь другим методом.')
        else:
            print('Ваше устройство выключено. Для добавления пользователя его нужно включить')


if __name__ == "__main__":
    # doctest.testmod()
    device = Device(model="Model", year_of_production=1993)
    print(device)
    print(device.__repr__())
    print(device.change_device_enable_status())
    device.create_user('user_name', 'user_password')
    device.create_user('wefwef', 13543151)
    print(device.change_device_enable_status())
    device.create_user('user_name', 'user_password')
    smartphone = SmartPhone(model="Model", year_of_production=1993, money_on_sim_card=53, user_number=71235321234)
    print(smartphone)
    print(smartphone.__repr__())
    print(smartphone.change_device_enable_status())
    smartphone.create_user('user_name', 'user_password')
    smartphone.money_on_sim_card = 100
    print(smartphone.change_device_enable_status())
    smartphone.create_user('user_name', 'user_password')
    computer = Computer(model="Model", year_of_production=1993, memory=53)
    print(computer)
    print(computer.__repr__())
    print(computer.change_device_enable_status())
    computer.create_user('user_name', 'user_password')
    computer.create_user('wefwef', 13543151)
