# can contains any type of data
# indexed, ordered, mutable
# allow duplicated members

from tkinter import Y


yearly_salaries = [
    120_000,
    72_000,
    57_000,
    98_000,
]

print(yearly_salaries)

data = [
    "John",
    10,
    True,
    None,
    "John",
    10,
    34.44,
    [1, 2, 3],
]
print(data)

print(len(yearly_salaries))

print(yearly_salaries[0])
print(yearly_salaries[3])
# IndexError: list index out of range
# print(yearly_salaries[10])

yearly_salaries[0] = 100_000
print(yearly_salaries)

print([1, 2, 3] + [4, 5, 6])
print([1, 2, 3] * 3)
