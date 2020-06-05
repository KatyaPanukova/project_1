from solution import *

Load.write('input.txt')
for i in Market.lst_products:
    print(i)
print(Product.max_price())
print(Product.total())
Product.del_product('3851211')
for i in Market.lst_products:
    print(i)
