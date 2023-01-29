from typing import Optional
from pydantic import BaseModel

from main1 import Book

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
# Импортировал класс Book из файла main1.py

# TODO написать класс Library

class Library(BaseModel):
    books: Optional[list[Book]]

    # def __init__(self, books=None):
    #     if books is None:
    #         self.books = []
    #     else:
    #         self.books = books

    def get_next_book_id(self):
        if self.books is None or self.books == []:
            return 1
        else:
            return self.books[-1].id_ + 1

    def get_index_by_book_id(self, id_number):
        for book in self.books:
            if id_number is book.id_:
                return self.books.index(book)
        else:
            raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки
    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
