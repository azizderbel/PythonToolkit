from functools import wraps
# A decorator is a function that takes another 
# function as an argument and extends its behavior 
# without changing the original function explicitly.


# the currency is a decorator of the fn function as it extends its fonctionalities
def currency(fn):
    @wraps(fn) # to retain the doculentation of the original function
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f'${result}'
    return wrapper

@currency
def net_price(price, tax):
    """ calculate the net price from price and tax
    Arguments:
        price: the selling price
        tax: value added tax or sale tax
    Return
        the net price
    """
    return price * (1 + tax)

print(net_price(100, 0.05))