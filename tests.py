from main import BooksCollector
import pytest

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2


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
        if len(book) == 0 or len(book) >= 41:
            expect = 0
        else:
            expect = 1
        assert len(collector.get_books_genre()) == expect

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
            ['Остров сокровищ', 'Мультфильмы'],
            ['Сияние', 'Ужасы']
        ])
    def test_get_books_for_children_added_to_list(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        if genre in collector.genre_age_rating:
            expect = []
        else:
            expect = [book]
        assert collector.get_books_for_children() == expect

    def test_add_book_in_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        expect = ['Гордость и предубеждение и зомби']
        assert collector.get_list_of_favorites_books() == expect

    def test_delete_book_from_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        expect = []
        assert collector.get_list_of_favorites_books() == expect

    def test_get_list_of_favorites_books_filled(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        expect = ['Гордость и предубеждение и зомби']
        assert collector.get_list_of_favorites_books() == expect
