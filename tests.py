from main import BooksCollector
import pytest

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_not_add_book_namelengh_more_then_41(self):
        collector = BooksCollector()
        collector.add_new_book('Как я перестал бояться и полюбил атомную бомбу')
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize(
        'book, genre',
        [
            ['Гордость и предубеждение и зомби', 'Комедии'],
            ['Остров сокровищ', 'Мультфильмы'],
            ['Сияние', 'Ужасы']
        ])
    def test_set_book_genre_setted_true(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == genre

    @pytest.mark.parametrize(
        'book, genre',
        [
            ['Гордость и предубеждение и зомби', 'Комедии'],
            ['Остров сокровищ', 'Мультфильмы'],
            ['Сияние', 'Ужасы']
        ])
    def test_get_book_genre_genre_by_name(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == genre

    @pytest.mark.parametrize(
        'book, genre',
        [
            ['Гордость и предубеждение и зомби', 'Комедии'],
            ['Остров сокровищ', 'Мультфильмы']
        ])
    def test_get_books_for_children_added_to_list(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_books_for_children() == [book]

    def test_get_books_for_children_not_added_to_list_by_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    def test_delete_book_from_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_filled(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']
