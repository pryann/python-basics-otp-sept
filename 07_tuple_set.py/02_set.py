# halmaz
# unordered, unindexed, unchangable
# not contains duplicated elements

my_set = {1, 2, 3}
print(my_set, type(my_set))

my_set.add(4)
print(my_set)

my_set.update([5, 6, 7])
print(my_set)

# not raise Error if the element not exists
my_set.discard(1)
print(my_set)

# raise Error if the element not exists
my_set.remove(2)
print(my_set)

my_set.pop()
print(my_set)

x1 = {"a", "b", "c"}
x2 = {"b", "c", "d"}

# unió
# operator: | : x1 | x2
print("unió: ", x1.union(x2))
# &
print("metszet: ", x1.intersection(x2))
# -
print("különbség: ", x1.difference(x2))
# ^
print("szimmetrikus különbség: ", x1.symmetric_difference(x2))
print("nincs-e közös metszet: ", {"z"}.isdisjoint(x2))
# <=
print("szülőhalmaza e: ", x1.issuperset({"a", "b"}))
# >=
print("részhalmaza e: ", {"a", "b"}.issubset(x1))
