# print
# type
# int
# float
# str
# range
# input
#
# https://docs.python.org/3/library/functions.html

# def_val = None

print(dir(__builtins__))


def greet(name):
    return f"Hello {name}"


print(greet("John"))
print(greet("Jane"))
print(greet("Bob"))

hi_jane = greet("Jane Doe")
print(hi_jane.upper())


# optional parameters at the end
def calculate_gross_price(net_price, vat_percent=27):
    return net_price * (1 + vat_percent / 100)


print(calculate_gross_price(1000))
print(calculate_gross_price(2000))
print(calculate_gross_price(3000))
print(calculate_gross_price(5000, 5))


# if you want to add default value to a mutable parameter: ALWAYS USE NONE!
def add_item_to_basket(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket


# basket = []
print(add_item_to_basket("apple"))
print(add_item_to_basket("banana"))
print(add_item_to_basket("orange"))
