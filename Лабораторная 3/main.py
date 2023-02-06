class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        if not isinstance(name, str):
            raise ValueError("Название книги должно быть строкового типа!")
        self._name = name
        if not isinstance(author, str):
            raise ValueError("Название автора должно быть строкового типа!")
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        """
        Я предпочел унаследовать метод str с небольшим дополнением о количестве страниц или длительности книги
        Использовал функцию super()
        """
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name=name, author=author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages):
        if new_pages <= 0:
            raise ValueError("Число страниц должно быть больше 0")
        if not isinstance(new_pages, int):
            raise TypeError(f"Число страниц должно быть типа int")
        self._pages = new_pages

    def __str__(self):
        return f"{super().__str__()}. Количество страниц {self.pages!r}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name=name, author=author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_length):
        if new_length <= 0:
            raise ValueError("Длительность книги должна быть больше 0")
        if not isinstance(new_length, float):
            raise TypeError(f"Длительность книги должна быть типа float")
        self._duration = new_length

    def __str__(self):
        return f"{super().__str__()}. Длительность книги {self.duration!r}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration!r})"


audiobook = AudioBook(name='Букварь', author='Пушкин', duration=2.1)
book = PaperBook('Букварь', 'Пушкин', 2)


print(audiobook)
print(book)
print(audiobook.__repr__())
print(book.__repr__())
