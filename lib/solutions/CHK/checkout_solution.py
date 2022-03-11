from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:

    price_table = {
        'A': (50, True), 
        'B': (30, True),
        'C': (20, False),
        'D': (15, False),
        'E': (40, True)}

    special_offers = {
        'A': [(3,20), (5,50)],
        'B': [(2,45)],
        'E': [(2,30)]}

    basket = Counter(skus)

    total_price = 0

    for item in basket:
        if item not in price_table:
            return -1
        price, any_special_offer = price_table[item]
        if any_special_offer:
            price, special_offer = price_table[item]
            count, offer_price = special_offer
            total_price += offer_price * (basket[item] // count)
            total_price += price * (basket[item] % count)
        else:
            total_price += calculate_price(price_table[item], basket[item])

    return int(total_price)

def calculate_price(price, count):
    return price * count

def calculate_special_offers(item, basket, special_offers, price_table):
    offer_total = 0
    if len(special_offers[item]) == 1:
        item_pack, discount = special_offers[item]
        offer_total += calculate_price(price_table[item], (basket[item] // item_pack))
        offer_total -= discount * (basket[item] // item_pack)
        offer_total += calculate_price(price_table[item], (basket[item] % item_pack))
    else:
        sorted_offers = sorted(special_offers[item], key=lambda tup: tup[1], reverse=True)
        for special_offer in special_offers:
            item_pack, discount = special_offer
            offer_total += calculate_price(price_table[item], (basket[item] // item_pack))
            offer_total -= discount * (basket[item] // item_pack)
            offer_total += calculate_price(price_table[item], (basket[item] % item_pack))
            #basket[item] -= 







