def apply_discount(item_name, price, promo_code):
    promo_code = promo_code.upper()
    if promo_code == "SAVE10":
        return price * 0.90
    elif promo_code == "HALFOFF":
        return price * 0.50
    else:
        return price