class Market:
    """The class describes the product."""

    sum_person = 0
    sum_all = 0
    max_val = 0
    val_price = []
    price_ = []

    def __init__(self, info, __data=' index: '):
        """Initialization method."""

        self.__num_buy = info[0]
        self.products = info[1]
        self.__data = __data or ' date: '

        for price in self.products:
            Market.sum_person += int(price[2])
            Market.val_price.append(int(price[2]))
            Market.price_.append(str(price[0]))

    def __set__data(self, __data):
        """The method of changing the values of the index date."""

        if '.' in self.products[0][1]:
            self.__data = ' date: '
        else:
            self.__data = ' index: '

        return self.__data

    def sum_buy(self):
        """Method of calculating the total sum of purchase."""

        sum_per = ''
        sum_per += 'Total sum: ' + str(Market.sum_person) + ' rubles.' + '\n'

        return sum_per

    def max_buy(self):
        """Method of searching for the maximum value of purchase."""

        maximum = ''
        product = ''
        Market.max_val = max(Market.val_price)
        product += str(Market.price_[Market.val_price.index(Market.max_val)])
        maximum += 'The most expensive thing in your purchase of ' + str(product) + ' is ' + str(Market.max_val) + '.'\
                   + '\n'

        return maximum

    def __str__(self):
        """String output method."""

        result = ''
        result += str(self.__num_buy) + '\n'
        count = 1
        for i in self.products:
            result += str(count) + ' ' + str(i[0]).capitalize() + self.__set__data(self.__data) + i[1] + ' price: ' + i[2] + '\n'
            count += 1

        return result

    def __repr__(self):
        """Output method."""

        return self.__str__()