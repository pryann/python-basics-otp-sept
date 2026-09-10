from random import randint, shuffle, choice

int_value = randint(1, 100)
print(int_value)

numbers = [1, 2, 3, 4, 5]
shuffle(numbers)
print(numbers)

pick = choice(numbers)
print(pick)
