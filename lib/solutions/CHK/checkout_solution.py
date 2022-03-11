from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:

    price_table = {
        'A': [50, (3,20), (5,50)], 
        'B': [30, (2,45)],
        'C': 20,
        'D': 15,
        'E': [40, (2,30)]}

    special_offers = {
        'A': [(3,20), (5,50)],
        'B': [(2,45)],
        'E': [(2,30)]}

    basket = Counter(skus)

    total_price = 0

    for item in basket:
        if item not in price_table:
            return -1
        if isinstance(price_table[item], list):
            price, special_offer = price_table[item]
            count, offer_price = special_offer
            total_price += offer_price * (basket[item] // count)
            total_price += price * (basket[item] % count)
        else:
            total_price += price_table[item] * basket[item]

    return int(total_price)

def calculate_special_offers(item, basket, price_table):
    






