from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    price_table = {
        'A': [50, (3,150)], 
        'B': [30, (2,45)],
        'C': 20,
        'D': 10}

    basket = Counter(skus)

    for item in basket:
        if item not in price_table:
            print('-1')

checkout('ABCDBCF')


