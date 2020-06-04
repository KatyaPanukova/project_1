from solution import *

with open('input.txt') as file:
    lines = file.readlines()
    dict_buyers = dict()
    list_a = []
    for value in lines:
        if 'Buyer' in value:
            dict_buyers[value[:-1]] = ()
            for i in lines[lines.index(value) + 1:]:
                if 'Buyer' not in i:
                    list_a.append(i[:-1].split())
                    dict_buyers[value[:-1]] += tuple([i[:-1].split()])
                else:
                    list_a.clear()
                    break
info = []
for buyer in dict_buyers:
    product = dict_buyers.get(buyer)
    info.append(buyer)
    info.append(product)

    pers = Market(info)
    print(pers)
    print(pers.sum_buy())
    print(pers.max_buy())
    info.clear()