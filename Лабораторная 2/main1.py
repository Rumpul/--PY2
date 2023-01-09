from pydantic import BaseModel, conint

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book(BaseModel):
    id_: conint(gt=0)
    name: str
    pages: conint(gt=0)

    # def __init__(self, id_: int, name: str, pages: int) -> None:
    #     """
    #     Создание объекта книга
    #
    #     :param id_: идентификатор книги
    #     :param name: название книги
    #     :param pages: количество страниц
    #
    #     """
    #     if not isinstance(id_, int):
    #         raise TypeError("ID книги должен быть целочисленным числом")
    #     if id_ <= 0:
    #         raise ValueError("ID книги не может быть меньше или равен 0")
    #     self.id_ = id_
    #     if not isinstance(name, str):
    #         raise TypeError("Название книги должно быть строкой")
    #     self.name = name
    #     if not isinstance(pages, int):
    #         raise TypeError("Количество страниц книги должно быть целочисленным числом")
    #     if pages <= 0:
    #         raise ValueError("Количество страниц книги не может быть меньше или равно 0")
    #     self.pages = pages

    def __str__(self) -> str:
        return f"Книга \"{self.name}\""

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id_={self.id_}, name=\'{self.name}\', pages={self.pages})"


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
