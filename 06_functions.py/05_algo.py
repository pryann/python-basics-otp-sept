# minimum kiválasztás


def get_minimum(values: list[int]) -> int:
    # feltételezem, hogy van legalább egy elem
    min_value = values[0]
    for value in values[1:]:
        if value < min_value:
            min_value = value
    return min_value


print(get_minimum([1, 2, 3, 4, 5]))
print(min([1, 2, 3, 4, 5]))


def get_maximum(values: list[int]) -> int:
    # feltételezem, hogy van legalább egy elem
    max_value = values[0]
    for value in values[1:]:
        if value > max_value:
            max_value = value
    return max_value


print(get_maximum([1, 2, 3, 4, 5]))
print(max([1, 2, 3, 4, 5]))


# összegzés
def summa(values):
    summa = 0
    for i in values:
        summa += i
    return summa


print(summa([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5]))


def avg(values):
    return summa(values) / len(values)


# megszámlálás


def get_count(values, search):
    count = 0
    for i in values:
        if i == search:
            count += 1
    return count


print(get_count([1, 2, 3, 4, 5, 3, 3, 4, 5], 3))
print([1, 2, 3, 4, 5, 3, 3, 4, 5].count(3))


# kiválasztás - tudjuk, hgoy benne van a listába, kell az indexe
def get_index(values, search):
    for i, v in enumerate(values):
        if v == search:
            return i


print(get_index([1, 2, 3, 4, 5, 3, 3, 4, 5], 3))
print([1, 2, 3, 4, 5, 3, 3, 4, 5].index(3))


# eldöntés : True, False


def is_contains(values, search):
    for i in values:
        if i == search:
            return True
    return False


print(is_contains([1, 2, 3, 4, 5], 3))
print(3 in [1, 2, 3, 4, 5])
