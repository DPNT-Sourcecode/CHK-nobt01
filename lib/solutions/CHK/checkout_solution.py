from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:

    price_table = {
        'A': [50, (3,150)], 
        'B': [30, (2,45)],
        'C': 20,
        'D': 10}

    basket = Counter(skus)

    total_price = 0

    for item in basket:
        if item not in price_table:
            return -1
        if isinstance(price_table[item], list):
            price, special_offer = price_table[item]
            count, offer_price = special_offer
            total_price += offer_price * (basket[item] / count)
            total_price += price * (basket[item] % count)
        else:
            total_price += price * basket[item]

    print(int(total_price))

checkout('AAABCDBC')




