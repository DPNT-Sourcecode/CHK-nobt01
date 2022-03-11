

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    price_table = {
        'A': [50, (3,150)], 
        'B': [30,
        'C': 20,
        'D': 10}

    for sku in skus:
        if sku not in 'ABCD':
            return -1

