BOOKS_DATABASE = [
    {
        "iden": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {   "iden": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

# TODO написать класс Book
class Book:
    def __init__(self, name: str, iden: int, pages: int):
        self.name = name
        self.iden = iden
        self.pages = pages
    def __str__(self) -> str:
        return f'Книга "{self.name}"'
    def __repr__(self) -> str:
        return f'Book(id_={self.iden}, name={self.name!r}, pages={self.pages})'

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(iden=book_dict["iden"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
        ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод repr