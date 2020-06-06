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
                    item = item.split()
                    Product.lst_products.append(Product(item[0], item[1], item[2], item[3]))



class Market:
    """The class describes the product."""

    lst_products = []

    def __init__(self, buyer, basket):
        """Initialization method."""
        self.buyer = buyer
        self.basket = basket

    @classmethod
    def max_check(cls):
        """Max check."""
        max_ = 0
        buyer = ''
        for i in cls.lst_products:
            dol = 0
            for j in i.basket:
                j = j.split()[-1]
                dol += int(j)
            if max_ < dol:
                buyer = str(i.buyer)
                max_ = dol

        return 'Client: {} purchased the goods in the amount {}.'.format(buyer, max_)

    @classmethod
    def return_check(cls, buyer, date, sale=None):
        """Return all check of your basket."""
        date_new = Date(date)
        total = 0
        result = ''
        for i in cls.lst_products:
            if str(i.buyer) == buyer:
                for j in i.basket:
                    total += int(j.split()[-1])
        if sale is not None and type(sale) == int:
            total_s = total - (total*int(sale)/100)
            result += '-' * 60 + '\n'
            result += '-' * 18 + 'Market "FAMILY_MARKET"' + '-' * 20 + '\n'
            result += 'Cash payment' + '\n'
            for item in cls.lst_products:
                if str(item.buyer) == buyer:
                    for j in item.basket:
                        tol = j.split()
                        result += str(Product(tol[0], tol[1], tol[2], tol[3]))
            result += '-' * 60 + '\n'
            result += 'Total without sale: {}\n'.format(total)
            result += 'Total with sale {} % : {} \n'.format(sale, total_s)
            result += 'Date: {} \n'.format(date_new)
            result += 'Thank you for the shopping!!!' + '\n'
            result += '-' * 60 + '\n'
        elif sale is None:
            result += '-'*60 + '\n'
            result += '-'*18 + 'Market "FAMILY_MARKET"' + '-'*20 + '\n'
            result += 'Cash payment' + '\n'
            for item in cls.lst_products:
                if str(item.buyer) == buyer:
                    for j in item.basket:
                        tol = j.split()
                        result += str(Product(tol[0], tol[1], tol[2], tol[3]))
            result += '-' * 60 + '\n'
            result += 'Total: {} \n'.format(total)
            result += 'Date: {} \n'.format(date_new)
            result += 'Thank you for the shopping!!!' + '\n'
            result += '-'*60 + '\n'

        return result

    def __str__(self):
        """String output method."""

        result = ''
        result += '{}'.format(self.buyer) + '\n'
        for item in self.basket:
            item = item.split()
            result += str(Product(item[0], item[1], item[2], item[3]))
        result += '\n'

        return result

    def __repr__(self):
        """Output method."""

        return self.__str__()


class Product:
    """Class described the product."""

    lst_products = []

    def __init__(self, name, code, date, price):
        """Initialization method."""
        self.name = name
        self.code = code
        self.date = date
        self.price = price

        dictionary = {'385': 'Switzerland', '460': 'Russia', '400': 'German', '009': 'USA', '045': 'Japan'}

        self.country = dictionary[self.code[:3]]

    @classmethod
    def add_product(cls, new):
        """Add new product in basket."""
        cls.lst_products.append(new)
        return 'Product add in basket.'

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

class Date:
    """"""
    date = None

    def __init__(self, __date):
        """"""
        self.__date = str(__date)
        self.dict_month = {'01': 'янв', '02': 'фев', '03': 'мар', '04': 'апр', '05': 'май', '06': 'июн',
                           '07': 'июл', '08': 'авг', '09': 'сен', '10': 'окт', '11': 'ноя', '12': 'дек'}
        self.dict_month_1 = {'01': 31, '02': 29, '03': 31, '04': 30, '05': 31, '06': 30,
                             '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}
        self.dict_month_2 = {'01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30,
                        '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}
        new_date = self.__date.split('.')

        if len(self.__date) != 10:
            if 0 > int(new_date[0]) > 31 or new_date[1] not in self.dict_month:
                print('ошибка')
                self.__date = None


    @property
    def date(self):
        """"""
        if self.__date is None:
            print('ошибка')
            return self.__date
        else:
            return self.__date

    @date.setter
    def date(self, new):
        """"""
        if new is not None:
            new_date = str(new).split('.')
            year = int(new_date[2])
            if len(new_date) == 10:
                if 0 > int(new_date[0]) > 31 or new_date[1] not in self.dict_month:
                    self.__date = None
                elif year % 4 != 0:
                    self.dict_month_1 = self.dict_month_2
                    if new_date[1] in self.dict_month and int(new_date[0]) <= self.dict_month_1[new_date[1]]:
                        self.__date = None
                else:
                    self.__date = new
            else:
                print('ошибка')
                self.__date = None
        else:
            self.__date = None

    @date.getter
    def date(self):
        """"""
        if self.__date is None:
            return None
        elif self.__date is not None:
            result = ''
            if isinstance(self.__date, str):
                list_inf = self.__date.split('.')
                n = 0
                for i in list_inf:
                    if n == 0:
                        day = i
                        if day[0] == 0:
                            day = day[1]
                        day = int(day)
                        result += str(day) + ' '
                    if n == 1:
                        month = i
                        result += self.dict_month[month] + ' '
                    if n == 2:
                        year = str(int(i))
                        result += year + ' г.'
                    n += 1
                return result

    def __repr__(self):
        """"""
        return str(self.date)
