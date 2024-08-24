import pytest
from main import BooksCollector

class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    '''def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2
'''
    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('book',
        [
         '',
         'Гордость и предубеждение и зомби',
         'Как я перестал бояться и полюбил атомную бомбу'
        ]
        )
    def test_add_new_book_add_book(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        lenght = 0 if len(book) == '' or len(book) >= 41 else 1
        assert len(collector.get_books_genre()) == lenght

    def test_set_book_genre_setted_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Комедии'

    def test_get_book_genre_genre_by_name(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Комедии'

    def test_get_books_for_children_added_to_list(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
        result = ['Гордость и предубеждение и зомби']
        assert collector.get_books_for_children() == result

    def test_add_book_in_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        #collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        result = ['Гордость и предубеждение и зомби']
        assert collector.get_list_of_favorites_books() == result

    def test_delete_book_from_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        # collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        result = []
        assert collector.get_list_of_favorites_books() == result

    def test_get_list_of_favorites_books_filled(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        # collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        result = ['Гордость и предубеждение и зомби']
        assert collector.get_list_of_favorites_books() == result
