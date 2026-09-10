# def is_even(num):
#     if num % 2 == 0:
#         return "even"
#     else:
#         return "odd"


# def is_even(num):
#     if num % 2 == 0:
#         return "even"
#     return "odd"


# python ternary (conditional expression), other lang: ? :
# def is_even(num):
#     return "even" if num % 2 == 0 else "odd"

# type annotations: ONLY FOR DOCUMENTATION
# BUT you can use tools to enforce type checking: mypy, pyright, ty.
# recommended: https://docs.astral.sh/ty/
def is_even(num: int) -> bool:
    return num % 2 == 0


print(is_even(3))
