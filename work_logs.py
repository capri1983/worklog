

def get_melon_order_price(price, quantity):
    """Calculate the cost for an order of melons."""

    tax = 0.075

    amount = price * quantity + (tax * price * quantity)

    print(amount)
