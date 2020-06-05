class Load:
    """Work with files."""
    @classmethod
    def write(cls, file):
        """Read the file."""
        with open(file) as file_1:
            lines = file_1.readlines()
            for i in lines:
                i = i[:-1]
                buyer = i.split(';')[0]
                basket = i.split(';')[1:]
                Market.lst_products.append(Market(buyer, basket))
                for item in basket:
                    Product.lst_products.append(Product(item.split()))


class Market:
    """The class describes the product."""

    lst_products = []

    def __init__(self, buyer, basket):
        """Initialization method."""
        self.buyer = buyer
        self.basket = basket

    def __str__(self):
        """String output method."""

        result = ''
        result += '{}'.format(self.buyer) + '\n'
        for item in self.basket:
            item = item.split()
            result += str(Product(item))
        result += '\n'

        return result

    def __repr__(self):
        """Output method."""

        return self.__str__()


class Product:
    """Class described the product."""

    lst_products = []

    def __init__(self, item):
        """Initialization method."""
        self.name = item[0]
        self.code = item[1]
        self.date = item[2]
        self.price = item[3]

        dictionary = {'385': 'Switzerland', '460': 'Russia', '400': 'German', '009': 'USA', '045': 'Japan'}

        self.country = dictionary[self.code[:3]]

    @staticmethod
    def max_price():
        """Maximal price."""
        max_value = 0
        cod_pro = ''
        for i in Product.lst_products:
            if int(i.price) > max_value:
                max_value = int(i.price)
                cod_pro = i.code

        return 'Max price of {}: {}\n'.format(cod_pro, int(max_value))

    @staticmethod
    def total():
        """Total sum for one buyer."""
        all = 0
        for i in Product.lst_products:
            all += int(i.price)

        return 'Total sum: {}\n'.format(int(all))

    @staticmethod
    def del_product(code):
        """Deleted object."""
        k = 0
        for i in Product.lst_products:
            if str(code) == str(i.code):
                del i.code
                k = 1
        if k == 1:
            print('Product with code: {} deleted.'.format(code))
        else:
            print('Product with code: {} not founded.'.format(code))

    def __str__(self):
        """String method."""
        s = ''
        s += '{} {} price: {} date: {} country: {}'.format(self.name, self.code, self.price, self.date,
                                                           str(self.country)) + '\n'

        return s

    def __repr__(self):
        """Output method."""
        return self.__str__()