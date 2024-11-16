class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int



    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        """
        Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        if self.quantity >= quantity:
            return True
        else:
            return False

    def buy(self, quantity):
        """
        реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if self.check_quantity(quantity):
            print("Продуктов достаточно")
            self.quantity = self.quantity - quantity
        else:
            raise ValueError("Не хватает продуктов на складе")

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:

    products: dict[Product, int]

    def get_products(self):
        print()
        for key, value in self.products.items():
            print(key.name, value)

        return self.products

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if product not in self.products:
            raise (ValueError('Такого продукта нет в корзине'))
        if remove_count is None or remove_count > self.products[product]:
            del self.products[product]
        else:
            self.products[product] -= remove_count

    def clear(self):
            self.products.clear()

    def get_total_price(self) -> float:
        total_price = 0
        for product, value in self.products.items():
            total_price += product.price * value
        return total_price

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        for product, value in self.products.items():
            if product.quantity < value:
                raise ValueError(f"Не хватает '{product.name}' на складе")

        for product, value in self.products.items():
            product.quantity -= value