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
        'E': [(2,'B')]}

    basket = Counter(skus)

    total_price = 0

    for item in basket:
        if item not in price_table:
            return -1
        price, any_special_offer = price_table[item]
        if any_special_offer:
            total_price += calculate_discount(item, basket, special_offers, price_table)
        else:
            total_price += calculate_price(price_table[item], basket[item])

    return int(total_price)

def calculate_giveaway(item, basket, special_offers):
    pass

def calculate_price(price, count):
    return price * count

def calculate_discount(item, basket, special_offers, price_table):
    offer_total = 0
    sorted_offers = sorted(special_offers[item], key=lambda tup: tup[0], reverse=True)
    for special_offer in sorted_offers:
        item_pack, discount = special_offer
        special_offer_entry = (basket[item] // item_pack)
        offer_total += calculate_price(price_table[item][0], special_offer_entry * item_pack)
        offer_total -= discount * (special_offer_entry)
        basket[item] -= special_offer_entry * item_pack

    offer_total += calculate_price(price_table[item][0], basket[item])

    return offer_total
        
print(checkout('AAAAAEE'))








