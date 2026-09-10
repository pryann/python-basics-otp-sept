# ordered, indexed
# immutable
# allow duplicates
# can contains any types of data
# TUPLE IS AN IMMUTABLE LIST

yearly_salaries = (120_000, 34_000, 98_000)
print(yearly_salaries, type(yearly_salaries))

print((1, 2, 3) + (4, 5, 6))
print((1, 2, 3) * 3)
print(len(yearly_salaries))
print(yearly_salaries.index(120_000))
print(yearly_salaries.count(120_000))
print(yearly_salaries[0])

# TypeError: 'tuple' object does not support item assignment
# yearly_salaries[0] = 0
rgb = (100, 255, 12)
coordinates = (45.234, 42.22344)

# fmt: off
one_elem_tuple = (123)
print(type(one_elem_tuple)) # int

one_elem_tuple = (123,)
print(type(one_elem_tuple)) # tuple

def stat(values):
  return min(values), max(values), sum(values)

result = stat([1,2,3,4,5,6,7])
print(result, type(result))
