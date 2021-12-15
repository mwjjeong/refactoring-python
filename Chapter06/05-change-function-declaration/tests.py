import math

from circum import circum
from book import Book


def test_circum():
    assert circum(3) == 2 * math.pi * 3


def test_book_add_reservation():
    book = Book()
    book.zz_add_reservation("Minwoo Jeong", False)
    assert "Minwoo Jeong" in book.reservations