"""
Протестируйте классы из модуля homework/models.py
"""

import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


@pytest.fixture
def iphone():
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
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1500) is False
        assert product.check_quantity(1) is True

    def test_product_buy(self, product):
        product.buy(700)

        assert product.quantity == 300

    def test_product_buy_more_than_available(self, product):
        with pytest.raises(ValueError) as excinfo:
            product.buy(7000)
        assert str(excinfo.value) in "Не хватает 6000 'book' на складе"
        assert product.quantity is 1000

        product.buy(900)
        assert product.quantity is 100

        product.buy(100)
        assert product.quantity is 0


class TestCart:
    """
     Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, cart, apple):
        cart.add_product(apple, buy_count=5)
        products = cart.products

        assert products.__len__() is 1
        assert products.get(apple) is 5

    def test_remove_product_error(self, cart, apple):
        with pytest.raises(ValueError) as excinfo:
            cart.remove_product(apple)
        assert str(excinfo.value) in "Продукта 'apple' нет в корзине"

    def test_remove_product_success(self, cart, apple, iphone, product):
        cart.add_product(apple, buy_count=5)
        cart.add_product(iphone, buy_count=5)
        cart.add_product(product, buy_count=5)

        cart.remove_product(apple)
        cart.remove_product(iphone, 2)
        cart.remove_product(product, 10)

        assert cart.products.get(apple) is None
        assert cart.products.get(iphone) is 3
        assert cart.products.get(product) is None
        assert cart.products.__len__() is 1

    def test_clear(self, cart, apple):
        cart.add_product(apple, 5)
        cart.clear()
        assert cart.products.__len__() is 0

    def test_get_total_price(self, cart, iphone, apple):
        cart.add_product(iphone)
        cart.add_product(apple, 15)
        assert cart.get_total_price() == 10150

    def test_buy_error(self, cart, iphone, apple):
        cart.add_product(iphone)
        cart.add_product(apple, 15)
        with pytest.raises(ValueError) as excinfo:
            cart.buy()
        assert str(excinfo.value) in "Не хватает 'apple' на складе"
        assert iphone.quantity is 10

    def test_buy_success(self, cart, iphone, apple):
        cart.add_product(iphone)
        cart.add_product(apple, 8)
        cart.buy()
        assert iphone.quantity is 9
        assert apple.quantity is 2
