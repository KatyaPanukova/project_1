from solution import *

Load.write('input.txt')
for i in Market.lst_products:
    print(i)
print(Product.max_price())
print(Product.total())
Product.del_product('3851211')
print(Product.add_product(Product('water', '04523312', '12.04.2020', '50')))
print(Market.max_check())
print(Market.return_check('Buyer 1', '06.06.2020', 15))
print(Market.return_check('Buyer 2', '27.05.2020'))
