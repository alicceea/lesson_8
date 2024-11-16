from models import Product, Cart


def m():
    # get -> возвращает значение по ключу
    # items -> возвращает пару ключ:значение
    # values -> возвращает все значения
    # keys -> возвращает все ключи

    cart = Cart()
    pen = Product('pen', 10, 'mmmmmm tasty 1', 2)
    pencil = Product('pencil', 10, 'mmmmmm tasty 2', 3)
    blank = Product('blank', 10, 'mmmmmm tasty 3', 5)

    print()
    list = [pen, pencil, blank]

    for i in list:
        if i.name == 'pencil':
            print(i.description)

    dictionary = {}  # key = str, value = Product
    for i in list:
        dictionary[i.name] = i
    # for k, v in dictionary.items():
    #    print(k, v)

    # у тебя есть название продукта, нужно найти его описание
    name = 'pencil'
    # for v in dictionary.values():
    #     print(v)
    #     if v.name == name:
    #         print(v.description)
    p = dictionary.get(name)
    print(p.description)

    # cart.add_product(pen)
    # cart.get_products()
    # cart.add_product(pen, buy_count=10)
    # cart.get_products()
    # cart.add_product(pencil, buy_count=2)
    # cart.get_products()
    # cart.add_product(blank)
    # cart.get_products()
    # cart.add_product(pen, buy_count=100)
    # cart.get_products()

# pen_value = cart.get_products().get(pen)
# print(pen_value)
