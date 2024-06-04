

class House(object):
    def __init__(self, price: float):
        # private class variable, also we can protect this by single underscore
        self.__price = price

    # getter, setter and deleter, we encapsulated this property
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        if price > 0 and isinstance(price, float):
            self.__price = price
        else:
            raise Exception('price is not valid')

    @price.deleter
    def price(self):
        del self.__price


if __name__ == '__main__':
    house = House(1600000.00)

    house.price = 1850000.00
    print(f'house price: {house.price}')

    house.__price = 0
    print(f'house new price: {house.price}')
