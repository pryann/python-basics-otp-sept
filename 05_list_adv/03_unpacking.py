abc = "abc"
a, b, c = abc
print(a, b, c)

first_name = "John"
last_name = "Doe"
age = 33

# more compact, readability is worse
first_name, last_name, age = "John", "Doe", 33

# data_swap
a = 10
b = 20

# tmp = a
# a = b
# b = tmp

a, b = b, a
print(a, b)

user = ["John", "Doe", 33, "mentor", ["reading", "writing"]]
first_name, last_name, *_ = user
print(first_name, last_name)

first_name, *rest, hobbies = user
print(first_name, hobbies)
