def test_add_new_book_add_two_books(self):
Вложенный первый тест изначально провальный. В файле main.py, в классе BooksCollector
отсутсвует метод get_books_rating.
Корректное выполнение теста возможно при добавлении в файл main.py метода get_books_rating добавлющего
проверку на self.genre_age_rating
Тест закомичен во время составления тестов для корректного написания остальных тестов
***
def test_add_new_book_add_book(self):
Тест проверяет добавление одной книге по названию.
***
def test_set_book_genre_setted_true(self):
тест на ввод жанра к названию книги

def test_get_book_genre_genre_by_name(self):
тест на вывод жанра книги по названию

def test_get_books_for_children_added_to_list(self):
Тест проверяет добавление в список по возрастному рейтингу
