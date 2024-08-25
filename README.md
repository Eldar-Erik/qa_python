# qa_python
Приветствую(!), уважаемый ревьюер. 

!Тесты запускал коммандой pytest tests.py --cov=main
!Вероятно слетел путь, ищу варианты решения.

def test_add_new_book_add_two_books(self):
Вложенный первый тест изначально провальный. В файле main.py, в классе BooksCollector
отсутсвует метод get_books_rating.
Корректное выполнение теста возможно при добавлении в файл main.py метода get_books_rating добавлющего
проверку на self.genre_age_rating
Тест закомментирован во время составления тестов для корректного написания остальных тестов
Раскомментирован к сдаче для чистоты кода.
***
def test_add_new_book_add_book(self):
Тест проверяет добавление одной книги по названию. попробовал добавить негативный тест через параметризацию
***
def test_set_book_genre_setted_true(self):
тест на ввод жанра к названию книги. добавлена параметризация
***
def test_get_book_genre_genre_by_name(self):
тест на вывод жанра книги по названию. добавлена параметризация
***
def test_get_books_for_children_added_to_list(self):
Тест проверяет добавление в список по возрастному рейтингу. добавлен негативный тест и параметризация
***
Блок тестов:\
def test_add_book_in_favorites_true(self): \
def test_delete_book_from_favorites_true(self):\
def test_get_list_of_favorites_books_filled(self):\
использовал простые вводные

