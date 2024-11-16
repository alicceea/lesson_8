"""
Протестируйте классы из модуля homework/models.py
"""
from pathlib import Path

import pytest
from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def cart():
    return Cart()

@pytest.fixture
def iphon():
    return Product('iphone', 10000, 'luxary', 10)

@pytest.fixture
def apple():
    return Product('apple', 10, 'luxary', 10)

class TestProducts():
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        assert True == product.check_quantity(-100)
        assert True == product.check_quantity(0)
        assert True == product.check_quantity(1000)
        assert False == product.check_quantity(1500)

    def test_product_buy(self, product):
        product.buy(700)

        assert 300 == product.quantity

    def test_product_buy_more_than_available(self, product):
        try:
            product.buy(7000)
        except ValueError:
            print('Превышено количество продуктов')

        assert 1000 == product.quantity


class TestCart:
    """
     Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, cart, apple):
        cart.add_product(apple, buy_count=5)
        products = cart.get_products()

        assert 1 == products.__len__()
        assert 5 == products.get(apple)

    def test_remove_product(self, cart, apple):
        hasError = False
        try:
            cart.remove_product(apple)
        except ValueError:
            hasError = True

        assert hasError

        cart.add_product(apple, buy_count=5)
        cart.remove_product(apple)
        assert 0 == cart.products.__len__()

        cart.add_product(apple,5)
        cart.remove_product(apple,2)
        assert 1 == cart.products.__len__()
        assert 3 == cart.products.get(apple)

        cart.add_product(apple, 5)
        cart.remove_product(apple, 10)
        assert 0 == cart.products.__len__()

    def test_clear(self, cart, apple):
        cart.add_product(apple, 5)
        cart.clear()
        assert 0 == cart.products.__len__()

    def test_get_total_price(self, cart, iphon, apple):
        cart.add_product(iphon)
        cart.add_product(apple, 15)
        assert 10150 == cart.get_total_price()

    def test_buy(self, cart, iphon, apple):
        cart.add_product(iphon)
        cart.add_product(apple, 15)
        hasError = False
        try:
            cart.buy()
        except ValueError:
            hasError = True

        assert hasError

        assert 10 == iphon.quantity

        cart.remove_product(apple, 8)
        cart.buy()
        assert 9 == iphon.quantity
        assert 3 == apple.quantity