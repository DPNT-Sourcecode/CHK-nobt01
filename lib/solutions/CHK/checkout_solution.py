from collections import Counter
from tokenize import group

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:

    price_table = {
        'A': (50, True), 
        'B': (30, True),
        'C': (20, False),
        'D': (15, False),
        'E': (40, True),
        'F': (10, True),
        'G': (20, False),
        'H': (10, True),
        'I': (35, False),
        'J': (60, False),
        'K': (70, True),
        'L': (90, False),
        'M': (15, False),
        'N': (40, True),
        'O': (10, False),
        'P': (50, True),
        'Q': (30, True),
        'R': (50, True),
        'S': (20, False),
        'T': (20, False),
        'U': (40, True),
        'V': (50, True),
        'W': (20, False),
        'X': (17, False),
        'Y': (20, False),
        'Z': (21, False)
    }

    discount_group = 'ZYSTX' 

    special_discounts = {
        'A': [(3, 20), (5, 50)],
        'B': [(2, 15)],
        'H': [(5, 5), (10, 20)],
        'K': [(2, 20)],
        'P': [(5, 50)],
        'Q': [(3, 10)],
        'V': [(2, 10), (3, 20)]
    }

    special_giveaways = {
        'E': [(2, 'B')],
        'F': [(3, 'F')],
        'N': [(3, 'M')],
        'R': [(3, 'Q')],
        'U': [(4, 'U')]
    }

    basket = Counter(skus)

    total_price = 0

    applied_group_discount = dict()

    for group_item in discount_group:
        if group_item in basket:
            discount_group = discount_group.get(group_item, 0) + 1
        

    for item in basket:
        if item not in price_table:
            return -1
        price, any_special_offer = price_table[item]
        if any_special_offer:
            if item in special_giveaways:
                total_price += calculate_with_giveaway(item, basket, special_giveaways, price_table)

    for item in basket:
        price, any_special_offer = price_table[item]
        if any_special_offer:
            if item in special_discounts:
                total_price += calculate_discount(item, basket, special_discounts, price_table)
        else:
            total_price += calculate_price(price, basket[item])

    return int(total_price)

def calculate_with_giveaway(item, basket, special_give_aways, price_table):
    offer_total = 0
    for special_offer in special_give_aways[item]:
        item_pack, giveaway = special_offer
        special_offer_entry = (basket[item] // item_pack)
        if giveaway in basket:
            basket[giveaway] -= special_offer_entry * 1
            if basket[giveaway] < 0:
                basket[giveaway] = 0

        offer_total += calculate_price(price_table[item][0], basket[item])
        basket[item] -= special_offer_entry * item_pack


    return offer_total



def calculate_price(price, count):
    return price * count

def calculate_discount(item, basket, special_discounts, price_table):
    offer_total = 0
    sorted_offers = sorted(special_discounts[item], key=lambda tup: tup[0], reverse=True)
    for special_offer in sorted_offers:
        item_pack, discount = special_offer
        special_offer_entry = (basket[item] // item_pack)
        offer_total += calculate_price(price_table[item][0], special_offer_entry * item_pack)
        offer_total -= discount * (special_offer_entry)
        basket[item] -= special_offer_entry * item_pack

    offer_total += calculate_price(price_table[item][0], basket[item])

    return offer_total





