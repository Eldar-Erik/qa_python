from main import BooksCollector


class BooksCollector:
    def __init__(self):
        self.books_genre = {}
        self.favorites = []
        self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        self.genre_age_rating = ['Ужасы', 'Детективы']


class TestBooksCollector:
    empty_list = []
    book_to_add = ['Крыса из нержавеющей стали']
    book_and_genre = (empty_list.append(book_to_add), self.genre[0])

print(book_and_genre())